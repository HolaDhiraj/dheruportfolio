
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.checks import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.messages import constants
from .models import ClientModel


# Create your views here.
def adminloginview(request):
    return render(request,"dheruapp/adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']
         
    user = authenticate(username = username, password = password)     

    #user exists
    if user is not None and user.username=="dhiraj1997":
        login(request,user)
        return redirect('adminhomepage')
    #user doesnot exists
    if user is None:
        #messages.add_message(request,messages.ERROR, "invalid credentials")
        #messages.info(request , 'invalid credentials')
        messages.add_message(request, constants.SUCCESS, 'Invalid_Credentials')
        return redirect('adminloginpage')

def adminhomepageview(request):
    
    return render(request,"dheruapp/adminhomepage.html")

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def homepageview(request):
    return render(request,"dheruapp/homepage.html")

def signupuser(request):
    username = request.POST['username']
    #email = request.POST['email']
    password =request.POST['password']
    Phone =  request.POST['Phone']
    #if username already exits
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"Username already exists")
        return redirect('homepage')


    #if username doesnot exits alredy (everything is fine to create user)
    User.objects.create_user(username = username, password = password).save()
    lastobject = len(User.objects.all())-1
    ClientModel(Userid = User.objects.all()[int(lastobject)].id, Phone = Phone,).save()
    messages.add_message(request,messages.ERROR,"User successfully created")
    return redirect('homepage')

def userloginview(request):
    return render(request,"dheruapp/userlogin.html")

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)     

        #user exists
    if user is not None:
        auth_login(request,user)
        return redirect('customerpage')

         #user doesnot exists
    if user is None:
        #messages.add_message(request,messages.ERROR,"Invalid_credentials")
        messages.info(request , 'invalid credentials')
        return redirect('userloginpage')
   
def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')



    username = request.user
    context = {'username': username, 'mobiles': ClientModel.objects.all()}
    return render(request,'dheruapp/customerwelcome.html',context)
    
def userlogout(request):
    logout(request)
    return redirect('userloginpage')