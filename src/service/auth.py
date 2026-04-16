from src.exceptions.custom_exceptions import Custom_Exception

class AuthService:

    @staticmethod
    def signup(payload , db):
        try:
            return 
        except Custom_Exception.RepositoryError as e:
            raise Custom_Exception.ServiceError('Error Encountered in Sevice Layer while creating user') from e