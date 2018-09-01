from tif.models.ioc_model import IOCModel
from tif.models.ioc import IOC
from tif.rest.auth import *

from flask import request, jsonify
from flask_restful import Resource

class Rest(Resource):
    def __init__(self):
        self.db = IOCModel()

    @auth.login_required
    def get(self):
        return jsonify(self.db.find())

    @auth.login_required
    def post(self):
        data = request.get_json(force=True)
        self.db.save(IOC(**data))
        return jsonify(data)
