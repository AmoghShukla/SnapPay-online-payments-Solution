class Custom_Exception:

    @staticmethod
    def RepositoryError(Exception):
        pass

    @staticmethod
    def ServiceError(Exception):
        pass

    @staticmethod
    def NotFoundError(RepositoryError):
        pass

custom_exp = Custom_Exception()