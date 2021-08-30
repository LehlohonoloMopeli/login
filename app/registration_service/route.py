from fastapi import APIRouter
from .model import RegistrationModel
from .service import Registration

router = APIRouter()

@router.post("/registration", tags=["Registration"])
async def registration_api(inputs : RegistrationModel):
    return Registration(inputs).register_user()
    