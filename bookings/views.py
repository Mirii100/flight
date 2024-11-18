from django.shortcuts import render,redirect
from .models import registerClient
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def book(request):
    return render(request,"index.html")

def results(request):
    
    regs=registerClient.objects.all()
    
    
    return render(request,"result.html",{"reg":regs})


def logout(request):
    
    regs=registerClient.objects.all()
    
    return render(request,"result.html",{"reg":regs})


def login(request):
    if request.method =='POST':
        userName=request.POST.get('userName',None)
        Email=request.POST.get('Email',None)
        password1=request.POST.get('password1',None)
        

        user=auth.authenticate(username=userName,email=Email,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request,'invalid credentials ')
            return redirect('login')


    
    else:

        return render(request,"login.html")


def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
            
        if password1==password2:
            if User.objects.filter(username=fname).exists():

                print('username already exit')
                messages.info(request,'username already taken')
                return render(request,'register')

            elif User.objects.filter(email=email).exists():
                print('email is already taken ')
                messages.info(request,'the email  entered is already taken ')
                return render(request,'register')



            else:

                user=User.objects.create_user(username=fname,password=password1,email=email)
                user.save()
                print('user created successfully')
                messages.info(request,'user created successfully ')
                return redirect('login')
            
        else:
            print('password mismatch ')
            messages.info(request,'there was a password mismatch ')
            return redirect('/')

    else:
        return render(request,"register.html")