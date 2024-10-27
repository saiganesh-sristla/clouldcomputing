from typing import Union

from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/login")

def login(user: User):
    print(user)
    if user.username == "pranay" and user.password == "1234":
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message" : "login successfully"})
    else:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content={"message" : "username or password incorrect"})
    