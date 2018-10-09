from pymongo import MongoClient
from tif.models.ioc import IOC

from datetime import datetime, timedelta
from configparser import ConfigParser

import os

class IOCModel:
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
        self.collection = self.db.iocs

    def save(self, ioc):
        exists = self.find_one(ioc)
        if not exists:
            self.collection.save(ioc.to_dict())

    def find_one(self, ioc):

        return self.collection.find(ioc.exists()).count()

    def find(self):
        iocs = list()
        for ioc in self.collection.find():
            iocs.append(IOC(**ioc))

        return iocs

    def find_by_key(self, key):
        iocs = list()
        for ioc in self.collection.find({key: {"$exists": True}}):
            iocs.append(IOC(**ioc))

        return iocs

    def find_by_key_value(self, key, value):
        iocs = list()
        cursor = self.collection.find({key: {"$regex" : ".*{}.*".format(value)}})
        for ioc in cursor:
            iocs.append(IOC(**ioc))

        return iocs

    def find_by_last_days(self, days):
        time = datetime.now() - timedelta(days)
        
        iocs = list()
        cursor = self.collection.find({"date": {"$gt" : time}})
        for ioc in cursor:
            iocs.append(IOC(**ioc))

        return iocs
