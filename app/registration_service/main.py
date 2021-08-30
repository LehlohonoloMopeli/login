from fastapi import FastAPI
from app.registration_service import route

"""
    To create virtual environment $: python -m venv env
    To activate virtual environment $: source ".\env\Scripts\activate"
    To install the requirements we run $: pip install -r requirements.txt
    To update requirements.txt after new pip install use $: pip freeze > requirements.txt
    To run  the program use the following command $: uvicorn app.registration_service.main:app --port 8001 --reload
    To deactivate virtual enviroment $: deactivate
    
"""

app = FastAPI()

app.include_router(route.router)


@app.get("/")
async def root():
    return "Registration Server"