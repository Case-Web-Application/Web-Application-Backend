from ninja import NinjaAPI, Schema, Router, File
from .models import *
from ninja.security import django_auth
import jwt
from jwt import decode, encode
from ninja.security import HttpBearer
from typing import List
from django.shortcuts import get_object_or_404
from testov.api_schema import *
from ninja.files import UploadedFile
from datetime import *
import datetime as datka
router = Router()

key = "super-s3cr3t--pass$word"

@router.delete("/delete_user")
def delete_user(request):
    users = User.objects.all()
    users.delete()
    return {"status":"200"}

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        return jwt.decode(token, key, algorithms="HS256")["login"]

@router.post("/auth")
def auth(request, payload: AuthIn):
    users = User.objects.filter(login=payload.login, password=payload.password)
    if len(list(users)) == 0:
        return {"response": "Неверный логин или пароль"}
    else:
        token = jwt.encode({"login": payload.login, "password": payload.password}, 
                           key, algorithm="HS256")
        return {"token": f"{token}"}

@router.post("/registration")
def registration(request, payload: RegisIn):
    employee = User.objects.create(**payload.dict())
    token = jwt.encode({"login": employee.login, 
                        "password": employee.password,
                        "number": employee.number,
                        "email": employee.email}, 
                         key, algorithm="HS256")
    tokens_create = Tokens.objects.create(user_id = employee.id, token1 = token)
    return f"{token}"

@router.post("/auth")
def auth(request, payload: AuthIn):
    users = User.objects.filter(login=payload.login, password=payload.password)
    if len(list(users)) == 0:
        return {"response": "Неверный логин или пароль"}
    else:
        token = jwt.encode({"login": payload.login, "password": payload.password}, 
                           key, algorithm="HS256")
        return {"token": f"{token}"}
    

@router.post("/make interpretation")
def make_interpr(request, payload: InterprIn):
    interpr = Interpretations.objects.create(**payload.dict())
    image = request.FILES['image']
    return f"{interpr.id}" 