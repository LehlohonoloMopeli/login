from app.database import Session
from .model import RegistrationModel
from app.database.user import User

from pyisemail import is_email
from fastapi.encoders import jsonable_encoder

class Registration:

    def __init__(self, inputs : RegistrationModel):
        self.__inputs = inputs
        self.session = Session()

    
    def register_user(self):

        sql = User(
            first_name = self.__inputs.first_name,
            surname = self.__inputs.surname,
            cell_number = self.__inputs.cell_number,
            email = self.__inputs.email,
            password = self.__inputs.password
        )

        #Validators

        if is_email(self.__inputs.email, check_dns=True) == False:
            return {
            "status": "failed",
            "message": "Email format is incorrect!"
        }

        if self.__inputs.password != self.__inputs.confirm_password:
            return {
            "status": "failed",
            "message": "Passswords do not match!"
        }

        query = self.session.query(User).filter_by(email = self.__inputs.email).first()

        if query is None !=True:
            return {
            "status": "failed",
            "message": "User already exists!"
            }

        self.session.add(sql)
        self.session.commit()

        return {
            "status": "passed",
            "message": "You have successfully registered!"
        }

