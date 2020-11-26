from infrastructure.exceptions import NotImplementError
from data.entities import Db


class DataSource:
    __instance = None

    def __init__(self):
        if DataSource.__instance is not None:
            raise Exception('the object has been Initialized')
        else:
            DataSource.__instance = DataSource.__connection()

    @staticmethod
    def __connection() -> Db:
        raise NotImplementError()

    @staticmethod
    def get_data_source():
        return DataSource.__instance
