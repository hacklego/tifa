class User():
    ''' '''

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.passwd = kwargs.get('passwd')

    def to_dict(self):
        return {self.name: self.passwd}

    def __str__(self):
        return str({self.name: self.passwd})
