from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Feature

def index(request):
    Feature1 = Feature()
    Feature1.id = 1
    Feature1.name = 'Fast'
    Feature1.details = 'Very quick'
    
    return render(request, 'index.html' , {'feature': Feature1})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        Email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=Email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=Email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not the same')
            return redirect('register')
    
    else:
        return render (request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')   
    
def logout(request):
    auth.logout(request)
    return redirect('index')    

def counter(request):
    if request.method == 'POST':
        text = request.POST.get('words', '')
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})
    return render(request, 'index.html')