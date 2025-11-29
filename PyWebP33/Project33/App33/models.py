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
    create_level = models.IntegerField(default=0)
    read_level = models.IntegerField(default=0)
    update_level = models.IntegerField(default=0)
    delete_level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.create_level}, {self.read_level}, {self.update_level}, {self.delete_level}))"


class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    login = models.CharField(User, max_length=32)
    salt = models.CharField(User, max_length=32)
    dk = models.CharField(User, max_length=32)


class AccessLog(models.Model):
    access_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Date and Time")
    response_code = models.PositiveSmallIntegerField(verbose_name="Status Code")

    def __str__(self):
        return f"{self.access_datetime} - {self.response_code}"

    class Meta:
        verbose_name = "Access to log"
        verbose_name_plural = "Access log"