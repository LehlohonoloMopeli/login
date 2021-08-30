from pydantic import BaseModel
from typing import Optional

class RegistrationModel(BaseModel):
    first_name: str
    surname: str
    cell_number: Optional[str] = None
    email: str
    password: str
    confirm_password: str
