from django.db import models

class registerpages(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    POSTION_CHOICES=[
        ('B','Begginer'),
        ('J','Junior'),
        ('S','Senior'),
    ]
    ABOUT_PYTHON_CHOICES=[
        ('F','From friends'),
        ('S','From Social media'),
        ('O','From other Source')
    ]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    position=models.CharField(max_length=100,choices=POSTION_CHOICES)
    Email=models.EmailField(max_length=100)
    years_of_experience=models.IntegerField()
    Gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    About_Python=models.CharField(max_length=1,choices=ABOUT_PYTHON_CHOICES)
    
def __str__(self):
    return self.first_name
    
    
    
