from tif.models.feed import Feed
from tif.models.feed_sync import FeedSynchronizer
from tif.models.feed_model import FeedModel

import requests
import re


class ZeusIp(FeedSynchronizer):
    def __init__(self):
        self.name = 'Zeus'
        self.uri = 'https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist'
        self.data = {'feed': self.uri, 'name': self.name}
        self.regex = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" 

    def sync(self):
        r = requests.get(self.uri)
        info = r.text.split('\n')
        db = FeedModel()
        for ip in info:
            if re.match(self.regex, ip):
                self.data['ip'] = ip
                feed = Feed(**self.data)
                db.save(feed)

                
class ZeusUrl(FeedSynchronizer):
    def __init__(self):
        self.name = 'Zeus'
        self.uri = 'https://zeustracker.abuse.ch/blocklist.php?download=compromised'
        self.data = {'feed': self.uri, 'name': self.name}
        self.regex = r".+\/.+\/"

    def sync(self):
        r = requests.get(self.uri)
        info = r.text.split('\n')
        db = FeedModel()
        for url in info:
            if re.match(self.regex, url):
                self.data['domain'] = url
                feed = Feed(**self.data)
                db.save(feed)
