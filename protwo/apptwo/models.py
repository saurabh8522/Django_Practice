from django.db import models

# Create your models here.
class User(models.Model):
    Fname= models.CharField(max_length=264)
    Lname=models.CharField(max_length=264)
    Email=models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.Email
