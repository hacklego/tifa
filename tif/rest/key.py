from tif.models.ioc_model import IOCModel

from flask_restful import Resource

class Key(Resource):
    def __init__(self):
        self.db = IOCModel()

    def get(self, ioc_key):
        return self.db.find_by_key(ioc_key)
