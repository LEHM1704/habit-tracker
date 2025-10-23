from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=64,unique=True)
    date_of_birth=models.DateField(null=True,blank=True)
    
    
    def __str__(self):
        return self.username
    
    
    