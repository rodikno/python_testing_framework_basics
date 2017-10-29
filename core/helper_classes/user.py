DEFAULT_USERNAME = 'myuser'
DEFAULT_PASSWORD = 'qazWSX123'
INCORRECT_PASSWORD = 'myincorrectpass'


class User(object):
    def __init__(self, username=None, password=None):
        self.username = username or DEFAULT_USERNAME
        self.password = password or DEFAULT_PASSWORD


class ValidUser(User):
    pass


class UserWithIncorrectPassword(User):
    def __init__(self, username=None):
        super().__init__(username)
        self.password = INCORRECT_PASSWORD
