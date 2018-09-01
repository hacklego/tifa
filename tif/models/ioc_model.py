from pymongo import MongoClient
from tif.models.ioc import IOC

from datetime import datetime, timedelta

class IOCModel:
    def __init__(self):
        self.client = MongoClient("mongodb://127.0.0.1:27017")
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
            iocs.append(str(IOC(**ioc)))

        return iocs

    def find_by_key(self, key):
        iocs = list()
        for ioc in self.collection.find({key: {"$exists": True}}):
            iocs.append(str(IOC(**ioc)))

        return iocs

    def find_by_key_value(self, key, value):
        iocs = list()
        cursor = self.collection.find({key: {"$regex" : ".*{}.*".format(value)}})
        for ioc in cursor:
            iocs.append(str(IOC(**ioc)))

        return iocs

    def find_by_last_days(self, days):
        time = datetime.now() - timedelta(days)
        
        iocs = list()
        cursor = self.collection.find({"date": {"$gt" : time}})
        for ioc in cursor:
            iocs.append(str(IOC(**ioc)))

        return iocs
