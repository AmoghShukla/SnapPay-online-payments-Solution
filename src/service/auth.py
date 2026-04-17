from src.model.user import User_Class, UserRole
from src.exceptions.custom_exceptions import Custom_Exception
from src.repository.user import UserRepository
from src.core.security import Security

class AuthService:

    @staticmethod
    def signup(payload , db):
        try:
            role = UserRole.USER if UserRepository.has_admin(db) else UserRole.ADMIN

            password = Security.hash_password(payload.user_password)

            user = User_Class(
                user_name = payload.user_name,
                user_contact_no = payload.user_contact_no,
                user_email = payload.user_email,
                user_password=password,
                user_role=role
            )

            return UserRepository.create_user(payload, db)
        except Custom_Exception.RepositoryError as e:
            raise Custom_Exception.ServiceError('Error Encountered in Sevice Layer while creating user') from e