from django.db import models

# Create your models here.
class Profile(models.Model):
   num = models.CharField(max_length = 10)
   path = models.CharField(max_length = 50)
   time = models.DateTimeField()
   def __str__(self):
    return self.num

