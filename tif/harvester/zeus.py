from tif.models.feed import Feed
from tif.models.ioc import IOC
from tif.models.ioc_model import IOCModel

import requests
import re


class ZeusIp(Feed):
    def __init__(self):
        self.name = 'Zeus'
        self.uri = 'https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist'
        self.data = {'feed': self.uri, 'name': self.name}
        self.regex = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" 

    def sync(self):
        r = requests.get(self.uri)
        info = r.text.split('\n')
        db = IOCModel()
        for ip in info:
            if re.match(self.regex, ip):
                self.data['ip'] = ip
                feed = IOC(**self.data)
                db.save(feed)

   
class ZeusUrl(Feed):
    def __init__(self):
        self.name = 'Zeus'
        self.uri = 'https://zeustracker.abuse.ch/blocklist.php?download=compromised'
        self.data = {'feed': self.uri, 'name': self.name}
        self.regex = r".+\/.+\/"

    def sync(self):
        r = requests.get(self.uri)
        info = r.text.split('\n')
        db = IOCModel()
        for url in info:
            if re.match(self.regex, url):
                self.data['domain'] = url
                feed = IOC(**self.data)
                db.save(feed)
