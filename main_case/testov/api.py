from ninja import NinjaAPI, Schema, Router
from .models import *
from ninja.security import django_auth
import jwt
import base64
from base64 import b64decode
from jwt import decode, encode
from ninja.security import HttpBearer


router = Router()
key = "super-s3cr3t--pass$word"


class UsersIn(Schema):
    login: str
    password: str
    first_name: str
    last_name: str
    age: int



@router.post("/registration")
def registration(request, payload: UsersIn):
    employee = User.objects.create(**payload.dict())
    token = jwt.encode({"id": employee.id, "login": employee.login, "password": employee.password}, key, algorithm="HS256")
    return f"{token}"

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        return jwt.decode(token, key, algorithms="HS256")["login"]


@router.get("/getusers", auth=AuthBearer())
def get_users(request):
    #id_user = request.auth
    all_users = User.objects.all()
    response = []
    for x in all_users:
        response.append({
            "Здравствуйте": request.auth,
            "id": x.pk,
            "login": x.login,
            "password": x.password,
            "first_name": x.first_name,
            "last_name": x.last_name,
            "age": x.age
        })
    return response

@router.get("/GetTast", auth=AuthBearer())
def get_tast(request):
    all_tasts = Tast.objects.all()
    response = []
    for x in all_tasts:
        response.append({
            f"Здравствуйте, {request.auth}"
            "id": x.pk,
            "name": x.name,
            "description_1": x.description_1,
            "description_2": x.description_2,
            "comments": x.comments,
            "time": x.time,
            "time_for_solve": x.time_for_solve,
            "status": x.status,
            "subtest": [f"Id: {x.subtest.id}", 
                        f"Субтест: {x.subtest.name}", 
                        f"Тема вопроса: {x.subtest.questions.name}",
                        f"Вопрос: {[i.description for i in Questions.objects.all()]}",
                        f"Ответ: {x.subtest.questions.answers.name}",
                        f"Описание ответа: {x.subtest.questions.answers.description}",
            ]
        })
    return response
