from tif.models.ioc_model import IOCModel
from tif.rest.auth import *

from flask_restful import Resource

class Rest(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self):
        return self.db.find()
