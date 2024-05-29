from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/signin/")
def home(request):
    return render(request, 'home.html')

@login_required(login_url="/login/signin/")
def parameters(request):
    return render(request, 'pages/parameters.html')

@login_required(login_url="/login/signin/")
def notifications(request):
    return render(request, 'pages/notifications.html')