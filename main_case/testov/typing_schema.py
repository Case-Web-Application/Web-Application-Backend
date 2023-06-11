from typing import List
from ninja import Schema

""" class Interpretations(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    text = models.CharField(max_length=255)#Добавить html разметку + картинки
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='files/covers', null=True)
    count_s = models.IntegerField()#20
    count_f = models.IntegerField()#40
    status = models.CharField(max_length=255)
 """
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