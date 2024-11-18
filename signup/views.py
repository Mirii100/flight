from django.shortcuts import render
from .models import Signup
# Create your views here.

def signUp(request):
    return render(request,"sign/signup.html")

def booking(request):
    reg=Signup.objects.all()
    return render(request,"sign/booking.html",{"reg":reg})

def reservation(request):
    return render(request,"sign/reserve.html")