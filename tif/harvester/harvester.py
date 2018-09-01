from tif.harvester.zeus import ZeusIp, ZeusUrl

class Harvester:

    feeds = [ZeusIp(), ZeusUrl()]
    
    @classmethod
    def sync_feeds(cls):
        for feed in cls.feeds:
            feed.sync()
