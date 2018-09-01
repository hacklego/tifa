from tif.models.ioc_model import IOCModel
from tif.rest.auth import *

from flask_restful import Resource

class Key(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self, ioc_key):
        return self.db.find_by_key(ioc_key)
