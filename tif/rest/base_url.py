from tif.models.ioc_model import IOCModel

from flask_restful import Resource

class Rest(Resource):
    def __init__(self):
        self.db = IOCModel()

    def get(self):
        return self.db.find()
