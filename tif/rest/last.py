from tif.models.ioc_model import IOCModel

from flask_restful import Resource

class Last(Resource):
    def __init__(self):
        self.db = IOCModel()

    def get(self, days):
        return self.db.find_by_last_days(days)
