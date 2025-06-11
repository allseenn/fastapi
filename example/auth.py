#!/usr/bin/env .venv/bin/python
# 11-4 Add a secret username and password to auth.py
import uvicorn
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

routes = APIRouter(prefix="/auth", tags=["Chapter 11. Authentication"])
security = HTTPBasic()

secret_user: str = "admin"
secret_password: str = "secret"

basic: HTTPBasicCredentials = HTTPBasic()

@routes.get("/who")
def get_user(
    credentials: HTTPBasicCredentials = Depends(basic)) -> dict:
    if (credentials.username == secret_user
        and credentials.password == secret_password):
        return { "username": credentials.username, "password": credentials.password }
    raise HTTPException(status_code=401, detail="Invalid credentials")


