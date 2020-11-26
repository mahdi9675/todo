from application.service import UserService


class Controller:

    def __init__(self,):
        pass


class UserController(Controller):

    def __init__(self):
        self.__service = UserService()

    def register(self, email, password):
        try:
            self.__service.register(email, password)
        except Exception as e:
            print(str(e))

    def login(self, email, password):
        try:
            self.__service.login(email, password)
        except Exception as e:
            print(str(e))

    def logout(self, token):
        try:
            self.__service.logout(token)
        except Exception as e:
            print(str(e))