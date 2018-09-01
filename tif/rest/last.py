from tif.models.ioc_model import IOCModel
from tif.rest.auth import *
from tif.formatters.formatter_factory import FormatterFactory

from flask import jsonify
from flask_restful import Resource

class Last(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self, days):
        cursor = self.db.find_by_last_days(days)
        iocs = [str(ioc) for ioc in cursor]
        return jsonify(iocs)

    
class LastFormat(Last):

    @auth.login_required
    def get(self, days, formatter):
        cursor = self.db.find_by_last_days(days)
        return FormatterFactory.format(cursor, formatter)
