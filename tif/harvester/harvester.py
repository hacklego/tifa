from tif.models.zeus import ZeusIp, ZeusUrl

class Harvester:

    feeds = [ZeusIp(), ZeusUrl()]

    '''
    @classmethod
    def register_feed(cls):
        def decorator(feed):
            cls.feeds.append(feed())
        return decorator
    '''
    
    @classmethod
    def sync_feeds(cls):
        for feed in cls.feeds:
            feed.sync()
