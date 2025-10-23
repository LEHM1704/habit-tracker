from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):   
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=64,unique=True)
    date_of_birth=models.DateField(null=True,blank=True)
    
    
    