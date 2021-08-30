from app.database import Session
from .model import RegistrationModel
from app.database.user import User


class Registration:

    def __init__(self, inputs : RegistrationModel):
        self.__inputs = inputs
        self.session = Session()

    
    def register_user(self):
        
