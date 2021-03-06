#  A web application that stores samples from a collection of NFC sensors.
#
#  https://github.com/cuplsensor/cuplbackend
#
#  Original Author: Malcolm Mackay
#  Email: malcolm@plotsensor.com
#  Website: https://cupl.co.uk
#
#  Copyright (c) 2021. Plotsensor Ltd.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the
#  GNU Affero General Public License along with this program.
#  If not, see <https://www.gnu.org/licenses/>.

# utils.py
from unittest.mock import Mock
from requests.models import Response
import json
import hmac
import hashlib
import base64
from wscodec.encoder.pyencoder.instrumented import InstrumentedSampleTRH


def create_capture_for_tag(response, baseurl, tagserial=None, tagsecretkey=None, tagerror=False, nsamples=10):
    if tagserial is None:
        tagserial = response.json()["serial"]
    if tagsecretkey is None:
        tagsecretkey = response.json()["secretkey"]
    capturetrh = InstrumentedSampleTRH(baseurl=baseurl,
                                       serial=tagserial,
                                       secretkey=tagsecretkey,
                                       tagerror=tagerror,
                                       smplintervalmins=10)
    samplesin = capturetrh.pushsamples(nsamples)
    queries = capturetrh.geturlqs()
    serial = queries['s'][0]
    statusb64 = queries['x'][0]
    timeintb64 = queries['t'][0]
    if 'q' in queries:
        circbufb64 = queries['q'][0]
    else:
        circbufb64 = ""
    vfmtb64 = queries['v'][0]
    outlist = {
            'serial': serial,
            'statusb64': statusb64,
            'timeintb64': timeintb64,
            'circbufb64': circbufb64,
            'vfmtb64': vfmtb64,
            'samplesin': samplesin
            }
    print(outlist)
    return outlist


def verifyhmac(response, wh_secretkey):
    content = json.loads(response.content)
    url_hmac_str = content['headers'].get('x-cuplbackend-hmac-sha256')[0]
    url_data_str = content['content']

    url_hmac_bytes = url_hmac_str.encode('utf-8')
    url_data_bytes = url_data_str.encode('utf-8')
    wh_secretkey_bytes = wh_secretkey.encode('utf-8')

    digest = hmac.new(wh_secretkey_bytes, url_data_bytes, hashlib.sha256).digest()
    computed_hmac_bytes = base64.b64encode(digest)
    assert url_hmac_bytes == computed_hmac_bytes


def strictkeyscheck(response, bodykeys):
    url_data_dict = json.loads(response.content)
    # A set comparison is done instead of a list comparison, because item order is irrelevant.
    bodykeys = set(bodykeys)
    urldictkeys = set(url_data_dict.keys())
    assert urldictkeys == bodykeys
