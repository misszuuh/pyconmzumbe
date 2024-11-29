from django import forms
from .models import *


class RegisterForm(forms.ModelForm):
      class Meta:
          model=registerpages
          fields=('first_name','last_name','position','Email','years_of_experience','Gender','About_Python')
          
          
          
