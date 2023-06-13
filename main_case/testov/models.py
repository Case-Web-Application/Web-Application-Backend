from django.db import models
from datetime import date


class User(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id}) {self.login}"
    
class Tokens(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token1 = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}"

class Interpretations(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', null=True)
    count_s = models.IntegerField()
    count_f = models.IntegerField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}) {self.name}"
    
class Scales(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    description = models.CharField(max_length=255)#Добавить html разметку + картинки
    interpretation = models.ForeignKey(Interpretations, on_delete=models.CASCADE)
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
    
    def __str__(self):
        return f"{self.id}) {self.name}"
    

class Answers(models.Model):
    name = models.CharField(max_length=255)
    queue = models.IntegerField()
    description = models.CharField(max_length=255)#Добавить html разметку + картинки
    scale = models.ForeignKey(Scales, on_delete=models.CASCADE)
    count_of_scale = models.IntegerField()
    right = models.BooleanField()
    status = models.CharField(max_length=255) 
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}) {self.name}"

    
class SubTest(models.Model):
    name = models.CharField(max_length=255)
    description_1 = models.CharField(max_length=255)
    description_2 = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
    time_for_solve = models.IntegerField()
    status = models.CharField(max_length=255)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}) {self.name}"

class Tast(models.Model):
    name = models.CharField(max_length=255)
    description_1 = models.CharField(max_length=255)
    description_2 = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
    time_for_solve = models.IntegerField()
    status = models.CharField(max_length=255)
    subtest = models.ForeignKey(SubTest, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}) {self.name}"

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

    def __str__(self):
        return f"{self.id}"