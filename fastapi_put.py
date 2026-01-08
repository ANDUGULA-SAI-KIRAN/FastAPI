from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app = FastAPI()

class user_data(BaseModel):
    name: str
    mobile: int
    Email:str

user_details= {}
user_id = 1

@app.post('/create_user')
def create_user(user_data:user_data):
    global user_id

    user_details[user_id] = user_data
    response = f"user id created successful : {user_id}" 
    user_id += 1
    return response

@app.get('/get_user')
def get_user():
    return user_details
