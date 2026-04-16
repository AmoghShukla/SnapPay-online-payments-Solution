from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from src.exceptions.custom_exceptions import Custom_Exception
from src.model.user import UserRole, User_Class


class UserRepository:

    @staticmethod
    def create_user(payload, db : Session):
        try:

            existing = UserRepository.check_user_by_email(payload.user_email)

            if existing:
                raise Custom_Exception.RepositoryError('User Already Exists!!')
            if isinstance(payload, User_Class):
                new_user = payload
                if new_user.user_role is None:
                    new_user.user_role = UserRole.USER
            else:
                role = payload.user_role if hasattr(payload, "user_role") and payload.user_role is not None else UserRole.USER
                new_user = User_Class(
                    user_name = payload.user_name,
                    user_email = payload.user_email,
                    user_password = payload.user_password,
                    user_contact_no = payload.user_contact_no
                )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            db.rollback()
            raise Custom_Exception.RepositoryError('Error while creating New User') from e

    
    @staticmethod
    def check_user_by_email(user_email , db : Session):
        try:
            db.query('User_Class').filter(User_Class.user_email==user_email).first()
        except SQLAlchemyError as e:
            raise Custom_Exception.RepositoryError('User Email-Id Not Found in Database') from e
        