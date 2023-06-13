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
router = Router()

key = "super-s3cr3t--pass$word"

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        return jwt.decode(token, key, algorithms="HS256")["login"]

@router.post("/registration")
def registration(request, payload: RegisIn):
    employee = User.objects.create(**payload.dict())
    token = jwt.encode({"id": employee.id,
                        "login": employee.login, 
                        "password": employee.password,
                        "number": employee.number,
                        "email": employee.email}, 
                         key, algorithm="HS256")
    tokens_create = Tokens.objects.create(user_id = employee.id, token1 = token)
    return f"{token}"

@router.post("/make interpretation")
def make_interpr(request, payload: InterprIn, file: UploadedFile = File()):
    interpr = Interpretations.objects.create(**payload.dict())
    return f"{interpr.id}"