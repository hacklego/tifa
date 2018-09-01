from tif.models.ioc_model import IOCModel
from tif.rest.auth import *

from flask_restful import Resource

class Last(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self, days):
        return self.db.find_by_last_days(days)
