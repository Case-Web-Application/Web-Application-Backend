from typing import List
from ninja import Schema
class UsersIn(Schema):
    login: str
    password: str
    first_name: str
    last_name: str
    number: str
    email: str
    age: int

class AnswersIn(Schema):
    name: str
    queue: int
    description: str
    count_of_scale: int
    right: int
    status: str  

class RegisIn(Schema):
    login: str
    password: str
    first_name: str
    last_name: str
    number: str
    email: str
    age: int

class QuestionIn(Schema):
    name: str
    queue: int
    type: str
    description: str
    obligatory: int
    mixq: int
    status: str
    answers_id: List[AnswersIn]