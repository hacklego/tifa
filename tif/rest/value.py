from tif.models.ioc_model import IOCModel
from tif.rest.auth import *
from tif.formatters.formatter_factory import FormatterFactory

from flask import jsonify
from flask_restful import Resource

class Value(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self, ioc_key, ioc_value):
        cursor = self.db.find_by_key_value(ioc_key, ioc_value)
        iocs = [str(ioc) for ioc in cursor]
        return jsonify(iocs)

    
class ValueFormat(Value):

    @auth.login_required
    def get(self, ioc_key, ioc_value, formatter):
        cursor = self.db.find_by_key_value(ioc_key, ioc_value)
        return FormatterFactory.format(cursor, formatter)
