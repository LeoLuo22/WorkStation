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

class House(models.Model):
    location
