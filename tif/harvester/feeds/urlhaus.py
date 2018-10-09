from tif.harvester.feed import Feed
from tif.models.ioc import IOC
from tif.models.ioc_model import IOCModel

import requests
import re
import csv


class URLHaus(Feed):
    def __init__(self):
        self.name = 'URLHaus'
        self.uri = 'https://urlhaus.abuse.ch/downloads/csv/'
        self.data = {'feed': self.uri, 'name': self.name}
        self.regex = r"^[^#]"

    def sync(self):
        r = requests.get(self.uri, timeout=60)
        info = csv.reader(r.content.decode('utf-8').splitlines())
        db = IOCModel()
        for line in info:
            if re.match(self.regex, line[0]):
                self.data['domain'] = line[2]
                self.data['threat'] = line[4]
                self.data['type'] = line[5]
                self.data['info'] = line[6]
                feed = IOC(**self.data)
                db.save(feed)
