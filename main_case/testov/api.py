from ninja import NinjaAPI, Schema, Router
from .models import *
from ninja.security import django_auth
import jwt
import base64
from base64 import b64decode
from jwt import decode
from ninja.security import HttpBearer
router = Router()

class UsersIn(Schema):
    login: str
    password: str
    first_name: str
    last_name: str
    age: int

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        key = "super-s3cr3t--pass$word"
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEiLCJsb2dpbiI6Ik1pa2UyMDA0IiwicGFzc3dvcmQiOiIxMjM0NTY3OCIsImZpcnN0X25hbWUiOiJNaWtoYWlsIiwibGFzdF9uYW1lIjoiTWFqb3JvdiIsImFnZSI6IjE4In0.lPCLFYeuPY8xC4AmULCBHqw_3ZJ_T-WYn67UWc8YcpA"
        return jwt.decode(token, key, algorithms="HS256")["id"]

#http://127.0.0.1:8000/api/v1/createuser
@router.post("/registration")
def registration(request, payload: UsersIn):
    employee = User.objects.create(**payload.dict())
    return {"id": employee.id}

#http://127.0.0.1:8000/api/v1/getusers
@router.get("/getusers", auth=AuthBearer())
def get_users(request):
    #id_user = request.auth
    all_users = User.objects.all()
    response = []
    for x in all_users:
        response.append({
            "id": x.pk,
            "login": x.login,
            "password": x.password,
            "first_name": x.first_name,
            "last_name": x.last_name,
            "age": x.age
        })
    return response

@router.get("/GetTast")
def get_tast(request):
    all_tasts = Tast.objects.all()
    response = []
    for x in all_tasts:
        response.append({
            "id": x.pk,
            "name": x.name,
            "description_1": x.description_1,
            "description_2": x.description_2,
            "comments": x.comments,
            "time": x.time,
            "time_for_solve": x.time_for_solve,
            "status": x.status,
            "subtest": [f"Id: {x.subtest.id}", 
                        f"Название: {x.subtest.name}", 
                        f"Тема: {x.subtest.questions.name}",
                        f"Вопрос: {x.subtest.questions.description}",
                        f"Ответ: {x.subtest.questions.answers.name}",
                        f"Описание: {x.subtest.questions.answers.description}",
            ]
        })
    return response