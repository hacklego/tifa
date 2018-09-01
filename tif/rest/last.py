from tif.models.ioc_model import IOCModel
from tif.rest.auth import *

from flask import jsonify
from flask_restful import Resource

class Last(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self, days):
        return jsonify(self.db.find_by_last_days(days))
