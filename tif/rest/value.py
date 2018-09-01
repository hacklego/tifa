from tif.models.feed_model import FeedModel

from flask_restful import Resource

class Value(Resource):
    def __init__(self):
        self.db = FeedModel()

        
    def get(self, ioc_key, ioc_value):
        return self.db.find_by_key_value(ioc_key, ioc_value)
