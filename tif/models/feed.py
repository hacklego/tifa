from datetime import datetime

class Feed():
    '''  '''

    def __init__(self, **kwargs):
        self.feed = kwargs.get('feed')
        self.date = kwargs.get('date', datetime.now().strftime("%Y-%B-%d"))
        self.type = kwargs.get('type',"")
        self.name = kwargs.get('name',"")
        self.hash = kwargs.get('hash',"")
        self.ip = kwargs.get('ip',"")
        self.domain = kwargs.get('domain',"")
        self.mail = kwargs.get('mail',"")
        self.artifact = kwargs.get('artifact',"")

    def to_dict(self):
        to_dict = dict()
        for k, v in self.__dict__.items():
            if v:
                to_dict[k] = v

        return to_dict

    def exists(self):
        exists = self.to_dict()
        exists.pop('date')
        return exists

    def __str__(self):
        return str(self.to_dict())
