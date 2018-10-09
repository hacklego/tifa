from pymongo import MongoClient
from tif.models.user import User

from configparser import ConfigParser

class UserModel:
    ''' '''

    def __init__(self):
        config_parser = ConfigParser()
        config_parser.read('tifa.conf')
        db = config_parser.get('tifa', 'db')
        self.client = MongoClient(db)
        self.db = self.client.tif
        self.collection = self.db.users

    def find(self):
        users = list()

        for user in self.collection.find():
            users.append(User(**user))

        return users

    def save(self, name, passwd):
        user = {"name": name, "passwd": passwd}
        self.collection.save(user)
