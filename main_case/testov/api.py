from ninja import NinjaAPI, Schema, Router
from .models import *

router = Router()


class UsersIn(Schema):
    login: str
    password: str
    first_name: str
    last_name: str
    age: int

#http://127.0.0.1:8000/api/v1/createuser
@router.post("/createuser")
def create_users(request, payload: UsersIn):
    employee = User.objects.create(**payload.dict())
    return {"id": employee.id}

#http://127.0.0.1:8000/api/v1/getusers
@router.get("/getusers")
def get_users(request):
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

