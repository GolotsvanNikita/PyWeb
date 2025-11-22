from django.db import models

# Create your models here.
# Моделі - це класи, призначені для відображення на базу даних
# є "представниками" таблиць у БД
class User(models.Model):
    first_name = models.CharField(max_length=64)   # name VARCHAR(64) | CHAR(64)
    last_name  = models.CharField(max_length=64)   
    email      = models.CharField(max_length=128)
    phone      = models.CharField(max_length=16)    
    birthdate  = models.DateField(null=True)  


class Role(models.Model):
    name = models.CharField(max_length=32)
    create_level = models.IntegerField
    read_level = models.IntegerField
    update_level = models.IntegerField
    delete_level = models.IntegerField


class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    login = models.CharField(User, max_length=32)
    salt = models.CharField(User, max_length=32)
    dk = models.CharField(User, max_length=32)