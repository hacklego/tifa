from tif.models.ioc_model import IOCModel
from tif.rest.auth import *
from tif.formatters.formatter_factory import FormatterFactory

from flask import jsonify
from flask_restful import Resource

class Key(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self, ioc_key):
        iocs = [str(ioc) for ioc in self.db.find_by_key(ioc_key)]
        return jsonify(iocs)

    
class KeyFormat(Key):
    @auth.login_required
    def get(self, ioc_key, formatter):
        return FormatterFactory.format(self.db.find_by_key(ioc_key), formatter)
