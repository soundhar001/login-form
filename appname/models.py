from django.db import models

# Create your models here.

class Login(models.Model):
    User_name = models.CharField(max_length = 50 , default="")
    Password = models.IntegerField(default="")


class SignUp(models.Model):
    Full_name = models.CharField(max_length = 50 , default="")
    Age = models.PositiveIntegerField(null=True, default="")
    Email = models.EmailField(max_length = 50 , default="")
    Phone = models.CharField(max_length = 10 ,null=True, default="")
    
