class NotImplementError(Exception):
    def __init__(self):
        super().__init__('method is not implement yet!')


class EmailValidationError(Exception):

    def __init__(self):
        super().__init__('Email is not in a valid form!')


class PasswordValidationError(Exception):

    def __init__(self):
        super().__init__('Password is not in a valid form!')


class CredentialError(Exception):

    def __init__(self):
        super().__init__('username or password is wrong!')


class AuthenticationError(Exception):

    def __init__(self):
        super().__init__('your are not authenticated!')