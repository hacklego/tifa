from datetime import datetime

class IOC():
    '''  '''

    def __init__(self, **kwargs):
        self.feed = kwargs.get('feed')
        self.date = kwargs.get('date', datetime.now())
        self.type = kwargs.get('type',"")
        self.name = kwargs.get('name',"")
        self.hash = kwargs.get('hash',"")
        self.ip = kwargs.get('ip',"")
        self.domain = kwargs.get('domain',"")
        self.mail = kwargs.get('mail',"")
        self.artifact = kwargs.get('artifact',"")
        self.info = kwargs.get('info', "")
        self.threat = kwargs.get('threat', "")
        self.asn = kwargs.get('asn', "")
        self.country = kwargs.get('country', "")
        self.isp = kwargs.get('isp', "")
        self.id = kwargs.get('_id')

    def to_dict(self):
        to_dict = dict()
        for k, v in self.__dict__.items():
            if v and k != 'id':
                to_dict[k] = v

        return to_dict

    def exists(self):
        exists = self.to_dict()
        exists.pop('date')

        return exists

    def __str__(self):
        to_str = self.to_dict()
        try:
            to_str['date'] = self.date.strftime("%Y-%B-%d")
        except:
            to_str['date'] = self.date

        return str(to_str)
