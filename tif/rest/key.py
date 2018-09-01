from tif.models.feed_model import FeedModel

from flask_restful import Resource

class Key(Resource):
    def __init__(self):
        self.db = FeedModel()

        
    def get(self, ioc_key):
        return self.db.find_by_key(ioc_key)
