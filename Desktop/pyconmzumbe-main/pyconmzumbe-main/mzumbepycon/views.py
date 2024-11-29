from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Homepage view
def homepage(request):
    return render(request, 'homepage.html')

# About page view
def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
       
       
         

    else: 
     form = RegisterForm()
    
    context={
        'form':form
    }
    
    return render(request,'register.html',context)          
        

