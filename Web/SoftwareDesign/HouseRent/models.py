from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    isMedium = models.BooleanField(default=False)

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
    isChecked = models.BooleanField(default=False)
    isWanted = models.BooleanField(default=False)

    def __str__(self):
        return self.username

