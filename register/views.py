from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
# Create your views here.

def Register(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 !=password2:
            context['error']= "Second password is wrong please checked"
            return render(request,'register/register.html',context)
        if first_name=="" or last_name=="" or user_name=="" or password1=="" or password2=="":
            context['error']="Check your information, pleace"
            return render(request,'register/register.html',context)
        user_check = User.objects.filter(username=user_name)
        if len(user_check)!=0:
            context['error']="This User already taken please other username"
            return render(request,'register/register.html',context)

        print('user created')
        user = User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        print(user_name,first_name)

        return render(request,'my_app/index.html')
    return render(request,'register/register.html')

def Signin(request):
    return render(request,'register/signin.html')
