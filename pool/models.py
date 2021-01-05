import datetime 
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tutors(models.Model):
        name = models.CharField(max_length = 100)
        disciple = models.CharField(max_length = 100)
        level = models.CharField(max_length = 100)
        
        def __str__(self):

                return f"{self.name}, {self.disciple}"


class Book(models.Model):
        title = models.CharField(max_length = 100)
        author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="books")
        lenght = models.IntegerField()

class Author(models.Model):
        name = models.CharField(max_length = 100)
        
class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        
        disciple = models.CharField(max_length = 100)
        level = models.CharField(max_length = 100)
        
        def __str__(self):
                return self.user.username



        # Create your models here.
