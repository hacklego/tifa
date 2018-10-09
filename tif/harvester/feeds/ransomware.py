from tif.harvester.feed import Feed
from tif.models.ioc import IOC
from tif.models.ioc_model import IOCModel

import requests
import re
import csv


class Ransomware(Feed):
    def __init__(self):
        self.name = 'Ramsomware'
        self.uri = 'https://ransomwaretracker.abuse.ch/feeds/csv/'
        self.data = {'feed': self.uri, 'type': 'ransomware'}
        self.regex = r"^[^#]"

    def sync(self):
        r = requests.get(self.uri, timeout=60)
        info = csv.reader(r.content.decode('utf-8', 'replace').splitlines())
        db = IOCModel()
        for line in info:
            if re.match(self.regex, line[0]):
                self.data['threat'] = line[1]
                self.data['name'] = line[2]
                self.data['domain'] = line[4]
                self.data['isp'] = line[5]
                self.data['ip'] = line[6]
                self.data['asn'] = line[7]
                self.data['country'] = line[8]
                feed = IOC(**self.data)
                db.save(feed)
