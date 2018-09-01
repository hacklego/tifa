from pymongo import MongoClient
from tif.models.feed import Feed

class FeedModel:
    def __init__(self):
        self.client = MongoClient("mongodb://127.0.0.1:27017")
        self.db = self.client.tif
        self.collection = self.db.feeds

    def save(self, feed):
        exists = self.find_one(feed)
        if not exists:
            self.collection.save(feed.to_dict())

    def find_one(self, feed):
        return self.collection.find(feed.exists()).count()
