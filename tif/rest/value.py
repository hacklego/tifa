from tif.models.ioc_model import IOCModel
from tif.rest.auth import *

from flask_restful import Resource

class Value(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self, ioc_key, ioc_value):
        return self.db.find_by_key_value(ioc_key, ioc_value)
