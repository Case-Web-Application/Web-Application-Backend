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

@router.post("/make attemption")
def make_attempt(request, payload: AtemptIn, 
    user_id: int, test_id: int,
    question_id: int, answers_id: int,
    scale_id: int, interpretation_id: int):
    attempt = Attemption.objects.create(
        number = payload.number,
        user = User.objects.get(id = user_id),
        tast = Tast.objects.get(id = test_id),
        question = Questions.objects.get(id = question_id),
        answers = Answers.objects.get(id = answers_id),
        scale = Scales.objects.get(id = scale_id),
        interpretation = Interpretations.objects.get(id = interpretation_id)
    )
    return {'status': 200}


@router.post("/make interpretation")
def make_interpr(request, payload: InterprIn, img_name: str, scale_id: int):
    interpr = Interpretations.objects.create(
        name = payload.name,
        queue = payload.queue,
        text = payload.text,
        image = Images.objects.get(title = img_name),
        count_s = payload.count_s,
        count_f = payload.count_f,
        status = payload.status,
        scale = Scales.objects.get(id = scale_id)
    )
    return {"status": 200}


@router.post("/make scales")
def make_scales(request, payload: ScalesIn, ans_id: int, img_name: str):
    scale = Scales.objects.create(
        name = payload.name,
        queue = payload.queue,
        description = payload.description,
        image = Images.objects.get(title = img_name),
        status = payload.status,
        answers = Answers.objects.get(id = ans_id)
    )
    return {"status": 200}  

@router.post("/make answers")
def make_answers(request, payload: AnswersIn, q_id: int, img_name: str):
    answer = Answers.objects.create(
        name = payload.name,
        queue = payload.queue,
        description = payload.description,
        image = Images.objects.get(title = img_name),
        count_of_scale = payload.count_of_scale,
        right = payload.right,
        status = payload.status,
        question = Questions.objects.get(id = q_id)
    )
    return {"status": 200}

@router.post("/make questions")
def make_question(request, payload: QuestionIn, img_name: str, subt_id: int):
    question = Questions.objects.create(
        name = payload.name,
        queue = payload.queue,
        type = payload.type,
        description = payload.description,
        image = Images.objects.get(title = img_name),
        obligatory = payload.obligatory,
        mixq = payload.mixq,
        status = payload.status,
        subtest = SubTest.objects.get(id = subt_id)
    )
    return {"status": 200}

@router.post("/make subtest")
def make_subtest(request, payload: SubTestIn, test_id: int):
    subtest = SubTest.objects.create(
        name = payload.name,
        description_1 = payload.description_1,
        description_2 = payload.description_2,
        comments = payload.comments,
        time = payload.time,
        time_for_solve = payload.time_for_solve,
        status = payload.status,
        test = Tast.objects.get(id = test_id)
    )
    return {'status': 200}

@router.get("/get_test")
def get_test(request):
    data = Interpretations.objects.all()
    response = []
    for x in data:
        response.append({
            'Test': x.scale.answers.question.subtest.test.name
        })