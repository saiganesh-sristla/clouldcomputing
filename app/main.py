from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from app.schema import User
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def home():  
    return {"Hello": "omkar"}

@app.post("/login")
def login(user:User):
    print(user)
    #DB read password for the username
    if user.username == "om" and user.password=="1234":
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message":"success"})
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content={"message":"failed"})

@app.get("/user/{user_id}")
def get_user_info(user_id:int):
    if user_id==4:
        data={
            "user_id":user_id,
            "first_name":"om",
            "last_name":"padwal",
            "email":"ompadwal@gmail.com"
        }

        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=data)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message":"user not found"})


@app.delete("/user/{user_id}")
def delete_user(user_id:int):
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message":"User deleted successfully"})

