from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from .models import *

LEVEL_CHOICES = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
]


class RegisterForm(UserCreationForm):
      
      class Meta:
           model=User
           fields=('username','password1','password2',)
                
        
           def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # Remove help texts for password fields
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = None
         
class LoginForm(AuthenticationForm):
    
  
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True,'class': 'form-control username-field',
            'placeholder': 'Enter your Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'autofocus': True,'class': 'form-control password-field',
            'placeholder': 'Enter your Password'}))
    
    
class RegisterUserForm(forms.ModelForm):
       Experience = forms.ChoiceField(
        choices=LEVEL_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
     

       class Meta:
           model=RegisterUser
           fields=('fullname','Course','year','Experience','Phone','Email','Student_ID')
            
            
           widgets = {
            'fullname': forms.TextInput(attrs={
                'autofocus': True,
                'class': 'form-control fullname-field',
                'placeholder': 'Enter your full name'
            }),
            'Course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your course'
            }),
            'year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your year'
            }),
            'Phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'Student_ID': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your student ID'
            }),
        }    
        
       
             