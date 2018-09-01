from tif.models.feed_model import FeedModel

from flask_restful import Resource

class Last(Resource):
    def __init__(self):
        self.db = FeedModel()

        
    def get(self, days):
        return self.db.find_by_last_days(days)
