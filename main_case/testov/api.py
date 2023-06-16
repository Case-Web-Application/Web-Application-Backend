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

@router.post("/make interpretation")
def make_interpr(request, payload: InterprIn):
    interpr = Interpretations.objects.create(**payload.dict())
    return {"status": 200}

@router.post("/make scales")
def make_scales(request, payload: ScalesIn, inter_id: int):
    scale = Scales.objects.create(
        name = payload.name,
        queue = payload.queue,
        description = payload.description,
        interpretation = Interpretations.objects.get(id = inter_id),
        status = payload.status)
    return {"status": 200}  

@router.post("/make questions")
def make_question(request, payload: QuestionIn):
    question = Questions.objects.create(**payload.dict())
    return {"status": 200}

@router.post("/make answers")
def make_answers(request, payload: AnswersIn, q_id: int, sc_id: int):
    answer = Answers.objects.create(
        name = payload.name,
        queue = payload.queue,
        description = payload.description,
        scale = Scales.objects.get(id = sc_id),
        count_of_scale = payload.count_of_scale,
        right = payload.right,
        status = payload.status,
        question = Questions.objects.get(id = q_id)
    )
    return {"status": 200}

""" @router.post("/make subtest")
def make_subtest(request, payload: SubTestIn, quest_id: int):
    subtest = SubTest.objects.create(
        name = payload.name,
        description_1 = payload.description_1,
        description_2 = payload.description_2,
        comments = payload.comments,
        time = payload.time,
        time_for_solve = payload.time_for_solve,
        status = payload.status,
        questions = Questions.objects.get(id = quest_id)
    )
 """

