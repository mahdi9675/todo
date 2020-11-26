from data.datasource import DataSource
from infrastructure.exceptions import NotImplementError


class Service:

    def __init__(self):
        self._ds = DataSource.get_data_source()


class UserService(Service):

    def login(self, username, password):
        raise NotImplementError()

    def register(self, username, password):
        raise NotImplementError()

    def logout(self, token):
        raise NotImplementError()
