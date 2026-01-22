from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field, EmailStr


app = FastAPI()

class user_data(BaseModel):
    name: str =Field(..., min_length=3, max_length=20)
    mobile: int
    Email:EmailStr

user_details= {}
user_id = 1

@app.post('/create_user')
def create_user(user_data:user_data):
    global user_id

    user_details[user_id] = user_data
    response = f"user id created successful : {user_id}, {user_data}" 
    user_id += 1
    return response

@app.get('/users')
def get_users():
    if not user_details:
        raise HTTPException(status_code=404, detail="No users found")
    return user_details

@app.get('/user/{user_id}')
def get_single_user(user_id: int):
    if user_id not in user_details:
        raise HTTPException(status_code=404, detail="User data not found")
    return user_details[user_id]

@app.put('/user/{user_id}')
def update_user(user_id:int, user_data:user_data):
    if user_id not in user_details:
        raise HTTPException(status_code=404, detail="User data not found")

    user_details[user_id] = user_data
    return {"message:": f"user id with {user_id} updated", "user_data": user_data}

@app.patch('/user/{user_id}')
def update_patch_user(user_id:int, user_data:user_data):
    if user_id not in user_details:
        raise HTTPException(status_code=404, detail="User data not found")

    user_details[user_id] = user_data
    return {"message:": f"user id with {user_id} updated", "user_data": user_data}

@app.delete('/user/{user_id}')
def delete_user(user_id:int):
    if user_id not in user_details:
        raise HTTPException(status_code=404, detail="User data not found")
    
    delete = user_details.pop(user_id) 
    return {"message": "user deleted", "user": delete}
    