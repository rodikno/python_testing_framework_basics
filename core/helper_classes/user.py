DEFAULT_USERNAME = 'myuser'
DEFAULT_PASSWORD = 'qazWSX123'


class User(object):
    def __init__(self, username=None, password=None):
        self.username = username or DEFAULT_USERNAME
        self.password = password or DEFAULT_PASSWORD
