from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=75)
    school = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    hours = models.IntegerField(max_length=1000)
    dateOfWork = models.IntegerField(max_length=10)
    dateOfEntry = models.IntegerField(max_length=10)

def __str__(self):
        return self.name