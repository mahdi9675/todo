class User:

    def __init__(self):
        self.id = ''
        self.email = ''
        self.password = '',
        self.token = ''


class ToDo:

    def __init__(self):
        self.id = ''
        self.userId = ''
        self.title = '',
        self.date = '',
        self.time = '',
        self.status = False


class Db:

    def __init__(self):
        self.content = dict(users=[], ToDos=[])
        # self.content = { 'users': [], 'ToDos': [] }
