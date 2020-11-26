from presentation.controller import UserController


if __name__ == '__main__':
    user = UserController()
    user.login('email@example.com', 'password')