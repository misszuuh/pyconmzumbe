from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login,logout

# Homepage view
def homepage(request):
    return render(request, 'homepage.html')

# About page view
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request,'index.html')

def Adminpage(request):
    if request.method == 'GET':
       form = RegisterUser.objects.all()
        
    context={
            'form':form,
        }
    return render(request,'Adminpage.html',context)




def Registerpage(request):
    if request.method=='POST':
      form=RegisterForm(request.POST)
      if form.is_valid():
          user=form.save()
          login(request,user)
          
          return redirect('Login')
      else:
         print(form.errors)
     
      
    else: 
     form = RegisterForm()
    
        
    
    context={
        'form':form,
       
    }
    
    return render(request,'Register.html',context)

def Loginpage(request):
    if request.method =='POST':
        form = LoginForm(request,data=request.POST)
        if form .is_valid():
            user =form.get_user()
            
            login(request,user)
            if user.username=='MUchapter@co.tz':
               return redirect('Adminpage')
            else:
                return redirect('MUchapter')
              
        
    else:
        
        form=LoginForm()
    context={
        'form':form,
    }         
    
    return render(request,'Login.html',context)

def UserReg(request):
    if request.method=='POST':
      form=RegisterUserForm(request.POST)
      if form.is_valid():
          user=form.save()
         
          
          return redirect('MUchapter')
      else:
         print(form.errors)
     
      
    else: 
     form = RegisterUserForm()
    
        
    
    context={
        'form':form,
       
    }
    
    return render(request,'UserRegister.html',context)

def code_of_conduct(request):
    return render(request, 'code_of_conduct.html')
