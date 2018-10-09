from tif.harvester.harvester import Harvester
from tif.harvester.feed import Feed
from tif.libs.importer import Importer

def get_feeds(path):
    feeds = Importer().import_subclasses_from_path(feeds_path, Feed)
    return [feed() for feed in feeds]

if __name__ == '__main__':
    feeds_path = 'tif/harvester/feeds'
    feeds = get_feeds(feeds_path)
    hv = Harvester(feeds)
    hv.sync_feeds()
