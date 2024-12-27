from fastapi import FastAPI, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional, Annotated


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") ##dependencia

@app.post("/token")

def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return form_data