from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('Adminpage/',views.Adminpage, name='Adminpage'),
    path('Register/',views.Registerpage, name='Register'),
    path('Login/',views.Loginpage, name='Login'),
    path('UserRegistration/',views.UserReg,name='UserRegistration'),
    path('code_of_conduct/',views.code_of_conduct,name='code_of_conduct')
    
    
]
