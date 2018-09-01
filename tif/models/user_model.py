from pymongo import MongoClient
from tif.models.user import User

class UserModel:
    ''' '''

    def __init__(self):
        self.client = MongoClient("mongodb://127.0.0.1:27017")
        self.db = self.client.tif
        self.collection = self.db.users

    def find(self):
        users = list()

        for user in self.collection.find():
            users.append(User(**user))

        return users
