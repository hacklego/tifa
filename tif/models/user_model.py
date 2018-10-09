from pymongo import MongoClient
from tif.models.user import User

from configparser import ConfigParser

import os

class UserModel:
    ''' '''

    def __init__(self):
        config_parser = ConfigParser()
        config_parser.read('tifa.conf')
        db = None
        try:
            db = config_parser.get('tifa', 'db')
        except:
            pass
        self.client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
        if db:
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
