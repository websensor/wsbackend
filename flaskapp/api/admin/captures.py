# Inspired by overholt
"""
    flaskapp.api.admin.boxes
    ~~~~~~~~~~~~~~

    Box endpoints
"""

from flask import Blueprint, request, jsonify, current_app
from flask_restful import Api, abort, reqparse
from ...services import captures
from ...captures.schemas import CaptureSchema
from ...core import ma
from marshmallow import fields, ValidationError
from .adminresource import SingleAdminResource, MultipleAdminResource


bp = Blueprint('admincaptures', __name__)
api = Api(bp)


class Capture(SingleAdminResource):
    """Get, modify or delete one box. """
    def __init__(self):
        super().__init__(CaptureSchema, captures)


class Captures(MultipleAdminResource):
    def __init__(self):
        super().__init__(CaptureSchema, captures)

    def get(self):
        """
        Get a list of captures.
        Returns:

        """
        return super().get_filtered(optfilterlist=['box_id'])

    def post(self):
        """
        Create a capture
        """
        jsondata = request.get_json()
        schema = self.Schema()
        try:
            schemaobj = schema.load(jsondata)
        except ValidationError as err:
            return err.messages, 422

        schemaobj = captures.save(schemaobj)

        return schema.dump(schemaobj)


api.add_resource(Capture, '/capture/<id>')
api.add_resource(Captures, '/captures')
