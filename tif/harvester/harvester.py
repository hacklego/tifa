from multiprocessing import Process

class Harvester:

    def __init__(self, feeds):
        self.feeds = feeds
    
    def sync(self, feed):
        feed.sync()

    def sync_feeds(self):
        processes = list()
        for feed in self.feeds:
            processes.append(Process(target=self.sync, args=(feed,)))

        for process in processes:
            process.start()

        for process in processes:
            process.join()
