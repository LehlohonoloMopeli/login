from app.database import Session
from .model import RegistrationModel
from app.database.user import User


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

        self.session.add(sql)
        self.session.commit()

        return {
            "status": "passed",
            "message": "You have successfully registered!"
        }
