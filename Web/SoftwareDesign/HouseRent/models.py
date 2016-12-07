from django.db import models

class NormalUser(models.Model):
    username = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Medium(models.Model):
    username = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class NormalHouse(models.Model):
    location = models.CharField(max_length=50)
    money = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    area = models.FloatField()
    description = models.TextField()
    picpath = models.CharField(max_length=100)
    time = models.DateField()
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class MediumHouse(models.Model):
    location = models.CharField(max_length=50)
    money = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    area = models.FloatField()
    description = models.TextField()
    picpath = models.CharField(max_length=100)
    time = models.DateField()
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username
