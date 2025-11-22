from django.db import models

# Create your models here.
# Моделі - це класи, призначені для відображення на базу даних
# є "представниками" таблиць у БД
class User(models.Model) :  
    first_name = models.CharField(max_length=64)   # name VARCHAR(64) | CHAR(64)
    last_name  = models.CharField(max_length=64)   
    email      = models.CharField(max_length=128)
    phone      = models.CharField(max_length=16)    
    birthdate  = models.DateField(null=True)  


class Role:
    name = models.CharField(max_length=32)
    create_level = models.IntegerField
    read_level = models.IntegerField
    update_level = models.IntegerField
    delete_level = models.IntegerField