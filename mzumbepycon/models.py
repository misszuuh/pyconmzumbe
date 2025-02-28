

from django.db import models
from django.contrib.auth.models import User

LEVEL_CHOICES= [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
]
 

class RegisterUser(models.Model):
        fullname=models.CharField(max_length=30)
        Course=models.CharField(max_length=30)
        year=models.CharField(max_length=4)
        Experience=models.CharField(max_length=30,choices=LEVEL_CHOICES,default='Begginer')
        Phone=models.CharField(max_length=15)
        Email=models.EmailField(max_length=30)
        Student_ID = models.CharField(max_length=12)
        
def __str__(self):
    return self.fullname
    
