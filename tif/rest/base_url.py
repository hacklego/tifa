from tif.models.ioc_model import IOCModel
from tif.rest.auth import *
from tif.formatters.formatter_factory import FormatterFactory

from flask import request, jsonify
from flask_restful import Resource

class Rest(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self):
        iocs = [str(ioc) for ioc in self.db.find()]
        return jsonify(iocs)

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        self.db.save(IOC(**data))
        return jsonify(data)


class RestFormat(Rest):

    @auth.login_required
    def get(self, formatter):
        return FormatterFactory.format(self.db.find(), formatter)
