""" from ninja import Schema, Router
from .models import *
from ninja.security import django_auth
import jwt
from jwt import decode, encode
from ninja.security import HttpBearer
from typing import List
from django.shortcuts import get_object_or_404
from typing_schema import * 
router = Router()
key = "super-s3cr3t--pass$word"

@router.post("/registration")
def registration(request, payload: RegisIn):
    employee = User.objects.create(**payload.dict())
    token = jwt.encode({
                        "login": employee.login, 
                        "password": employee.password,
                        "number": employee.number,
                        "email": employee.email},
                         key, algorithm="HS256")
    tokens_create = Tokens.objects.create(user_id = employee.id, token1 = token)
    return f"{token}"

@router.post("/make interpretation")
def interpretations(request, ) """