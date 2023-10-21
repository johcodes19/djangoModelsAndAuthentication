from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#if the request object is not authenticated....
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    
def login_view(request):
    return render(request, 'users/login.html')

def logout_view(request):
    pass