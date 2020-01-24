import pytest
import pytz
import datetime


def create_capture_get_samples(capturespeclist, boxwithcaptures, samplewrapper):
    bwc = boxwithcaptures.get(capturespeclist)

    box = bwc['box']
    clisthelper = bwc['clisthelper']

    captures_in = clisthelper.writtencaptures
    starttime = clisthelper.mints
    endtime = clisthelper.maxts

    samples_out = samplewrapper.get_samples(box['serial'], starttime, endtime)
    return captures_in, samples_out


def test_samples(box_with_captures_fixture, sample_fixture):
    starttime = datetime.datetime.now().replace(tzinfo=pytz.utc)
    capturespeclist = [
        {
            'starttime': starttime,
            'nsamples': 4
        },
        {
            'starttime': starttime+datetime.timedelta(seconds=2),
            'nsamples': 5
        }
    ]
    captures_in, samples_out = create_capture_get_samples(capturespeclist, box_with_captures_fixture, sample_fixture)

    # Newest to oldest order
    expectedsamples = [
        captures_in[1]['samples'][0],
        captures_in[0]['samples'][0],
        captures_in[0]['samples'][1],
        captures_in[0]['samples'][2],
        captures_in[0]['samples'][3],
        ]

    print(expectedsamples)
    print(samples_out)
    assert expectedsamples == samples_out


def test_samples_two(box_with_captures_fixture, sample_fixture):
    starttime = datetime.datetime.now().replace(tzinfo=pytz.utc)
    capturespeclist = [
        {
            'starttime': starttime,
            'nsamples': 4
        },
    ]
    captures_in, samples_out = create_capture_get_samples(capturespeclist, box_with_captures_fixture, sample_fixture)

    expectedsamples = [
        captures_in[0]['samples'][0],
        captures_in[0]['samples'][1],
        captures_in[0]['samples'][2],
        captures_in[0]['samples'][3]
        ]

    print(expectedsamples)
    print(samples_out)
    assert expectedsamples == samples_out


if __name__ == "__main__":
    pytest.main()
