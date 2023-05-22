
from django.db import models

class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    
class Answers(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    description = models.CharField(max_length=255)
    #TODO

class Questions(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    obligatory = models.IntegerField()
    mixq = models.IntegerField()
    status = models.CharField(max_length=255)
    answers = models.ForeignKey(Answers, on_delete=models.CASCADE)


class SubTest(models.Model):
    name = models.CharField(max_length=255)
    description_1 = models.CharField(max_length=255)
    description_2 = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
    time_for_solve = models.IntegerField()
    status = models.CharField(max_length=255)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)

class Test(models.Model):
    name = models.CharField(max_length=255)
    description_1 = models.CharField(max_length=255)
    description_2 = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
    time_for_solve = models.IntegerField()
    status = models.CharField(max_length=255)
    subtest = models.ForeignKey(SubTest, on_delete=models.CASCADE)