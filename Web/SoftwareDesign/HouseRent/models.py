from django.db import models

class NormalUser(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.EmailField()

class Medium(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    #email = models.EmailField()
