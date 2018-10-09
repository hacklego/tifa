from tif.harvester.harvester import Harvester
from tif.harvester.feed import Feed
from tif.libs.importer import Importer

from configparser import ConfigParser

def get_feeds():
    config_parser = ConfigParser()
    config_parser.read('tifa.conf')
    feeds_path = config_parser.get('tifa', 'feeds')
    feeds = Importer().import_subclasses_from_path(feeds_path, Feed)
    return [feed() for feed in feeds]

if __name__ == '__main__':
    feeds = get_feeds()
    hv = Harvester(feeds)
    hv.sync_feeds()
