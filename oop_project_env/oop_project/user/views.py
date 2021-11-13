from django.shortcuts import render

# Create your views here.

def index(request):
    # Your Code
    return render(request, 'user/index.html') 

def signIn(request):
    # Your Code
    return render(request, 'user/login.html') 

def signUp(request):
    # Your Code
    return render(request, 'user/register.html') 

