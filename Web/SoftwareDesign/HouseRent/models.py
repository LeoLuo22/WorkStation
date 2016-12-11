from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    isMedium = models.BooleanField(default=False)
    isChecked = models.BooleanField(default=True)
    owner = models.CharField(max_length=16, default="")
    paper = models.CharField(max_length=16, default="")
    taxpaper = models.CharField(max_length=16, default="")
    paperpic = models.CharField(max_length=100, default="")
    idpic = models.CharField(max_length=100, default="")
    isadmin = models.BooleanField(default=False)
    bookedhouse = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class House(models.Model):
    location = models.CharField(max_length=50)
    money = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    area = models.FloatField()
    description = models.TextField()
    picpath = models.CharField(max_length=100)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    isWanted = models.BooleanField(default=False)
    isMedium = models.BooleanField(default=False)
    isBooked = models.BooleanField(default=False)
    def __str__(self):
        return self.location

