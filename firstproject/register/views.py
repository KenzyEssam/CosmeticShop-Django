from django.shortcuts import render,redirect,HttpResponse 
from django.contrib.auth.models import User


def login(request):
    return render(request,'register/login.html')





def signup(request):

   

    return render(request,'register/signup.html')






