from django.db import models
from datetime import date

class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id}) {self.login}"
    
class Interpretations(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    text = models.CharField(max_length=255)#Добавить html разметку + картинки
    count_s = models.IntegerField()
    count_f = models.IntegerField()
    status = models.CharField(max_length=255)

class Scales(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    description = models.CharField(max_length=255)#Добавить html разметку + картинки
    interpretation = models.ForeignKey(Interpretations, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

class Answers(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    description = models.CharField(max_length=255)#Добавить html разметку + картинки
    scale = models.ForeignKey(Scales, on_delete=models.CASCADE)
    count_of_scale = models.IntegerField()
    right = models.IntegerField()
    status = models.CharField(max_length=255) 

class Questions(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)#Добавить html разметку + картинки
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

class Tast(models.Model):
    name = models.CharField(max_length=255)
    description_1 = models.CharField(max_length=255)
    description_2 = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
    time_for_solve = models.IntegerField()
    status = models.CharField(max_length=255)
    subtest = models.ForeignKey(SubTest, on_delete=models.CASCADE)

class Attemption(models.Model):
    number = models.IntegerField()
    date = models.DateField(default=date.today)
    time_s = models.DateTimeField(auto_now=True)
    #time_f = models.DateTimeField(auto_now=True) Тригеррится при ответе на последний вопрос
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tast = models.OneToOneField(Tast, on_delete=models.CASCADE)
    question = models.OneToOneField(Questions, on_delete=models.CASCADE)
    answers = models.OneToOneField(Answers, on_delete=models.CASCADE)
    scale = models.OneToOneField(Scales, on_delete=models.CASCADE)
    interpretation = models.OneToOneField(Interpretations, on_delete=models.CASCADE)
