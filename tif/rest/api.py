from tif.models.feed_model import FeedModel

from flask_restful import Resource

class Rest(Resource):
    def __init__(self):
        self.db = FeedModel()

        
    def get(self):
        return self.db.find()
