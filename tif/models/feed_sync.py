class FeedSynchronizer:

    def __init__(self):
        self.name = ''
        self.uri = ''
        self.data = ''
        self.regex = ''
        
    def sync(self):
        print('Updating feed: {}'.format(self.__class__))
