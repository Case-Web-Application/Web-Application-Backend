from ninja import NinjaAPI, Schema, Router
from .models import *
from ninja.security import django_auth
import jwt
import base64
from base64 import b64decode
from jwt import decode, encode
from ninja.security import HttpBearer
from typing import List
from django.shortcuts import get_object_or_404

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

@router.post("/make_quest")
def questions(request, payload: QuestionIn):
    for y in Answers.objects.all():
        anwsers = get_object_or_404(Answers, name=y.name)
        employee = Questions.objects.create(
            name = payload.name,
            queue = payload.queue,
            type = payload.type,
            description = payload.description,
            obligatory = payload.obligatory,
            mixq = payload.mixq,
            status = payload.status,
            answers = anwsers
        )
    return f"ID вопроса - {employee.id}"

@router.get("/getans")
def get_ans(request):
    all_ans = Answers.objects.all()
    response = []
    for x in all_ans:
        response.append({
            "id": x.pk,
            "name": x.name,
            "queue": x.queue,
            "description": x.description,
            "scale": x.scale,
            "count_of_scale": x.count_of_scale,
            "right": x.right,
            "status": x.status
            })
    ans = []
    for y in Answers.objects.all():
        names = y.name
        anwsers = get_object_or_404(Answers, name=names)
        ans.append(anwsers)
    return f"{ans}"

@router.get("/getquest")
def get_users(request):
    all_quest = Questions.objects.all()
    response = []
    for x in all_quest:
        response.append({
            "id": x.pk,
            "name": x.name,
            "queue": x.queue,
            "type": x.type,
            "description": x.description,
            "obligatory": x.obligatory,
            "mixq": x.mixq,
            "status": x.status,
            "answers": x.answers})
    return f"{response}"


#http://127.0.0.1:8000/api/v1/getusers
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

""" class Answers(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    description = models.CharField(max_length=255)#Добавить html разметку + картинки
    #scale = models.ForeignKey(Scales, on_delete=models.CASCADE)
    count_of_scale = models.IntegerField()
    right = models.BooleanField()
    status = models.CharField(max_length=255) 

    def __str__(self):
        return f"{self.id}) {self.name}"
    
class Questions(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)#Добавить html разметку + картинки
    obligatory = models.BooleanField()
    mixq = models.BooleanField()
    status = models.CharField(max_length=255)
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE, null=True) """

class AnswersIn(Schema):
    name: str
    queue: int
    description: str
    count_of_scale: int
    right: int
    status: str  

class QuestionIn(Schema):
    name: str
    queue: int
    type: str
    description: str
    obligatory: int
    mixq: int
    status: str
    answers_id: List[AnswersIn]
 
  

@router.post("/make_answer")
def make_answers(request, payload: QuestionIn):
    pass

