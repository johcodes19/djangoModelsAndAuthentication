from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#if the request object is not authenticated....
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request,'users/user.html' )
    
def login_view(request):
    #if the request method is POST, first get the username and password
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        #to authenticate the user, 
        user= authenticate(request, username=username, password=password)
        #if the user is authenticated or not None,.... log them in and return them to index 
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        #if the user is not authenticated, return the login form with a message saying invalid credentials
        else:
            return render(request, 'users/login.html',{
                'message': 'Invalid credentials'
            })
    return render(request, 'users/login.html')

def logout_view(request):
    pass