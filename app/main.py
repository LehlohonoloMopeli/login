from fastapi import FastAPI

"""
    To create virtual environment $: python -m venv env
    To activate virtual environment $: source ".\env\Scripts\activate"
    To install the requirements we run $: pip install -r requirements.txt
    To update requirements.txt after new pip install use $: pip freeze > requirements.txt
    To run  the program use the following command $: uvicorn app.main:app --port 8000 --reload
    To deactivate virtual enviroment $: deactivate
    
"""

app = FastAPI()

from app.registration_service import route
app.include_router(route.router)


@app.get("/")
async def root():
    return "Sizwe's server"
