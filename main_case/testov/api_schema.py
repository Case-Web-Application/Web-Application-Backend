from typing import List
from ninja import Schema

class TestIn(Schema):
    name: str
    description_1: str
    description_2: str
    comments: str
    time_for_solve: int
    status: str

class AuthIn(Schema):
    login: str
    password: str


class InterprIn(Schema):
    name: str 
    queue: int
    text: str
    image: str 
    count_s: int
    count_f: int
    status: str

class ScalesIn(Schema):
    name: str
    queue: int
    description: str
    status: str
    
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

class SubTestIn(Schema):
    name: str
    description_1: str
    description_2: str
    comments: str
    time_for_solve: int
    status: str