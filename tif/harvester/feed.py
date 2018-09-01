class Feed:

    def __init__(self):
        self.name = ''
        self.uri = ''
        self.data = ''
        self.regex = ''
        
    def sync(self):
        raise NotImplementedError
