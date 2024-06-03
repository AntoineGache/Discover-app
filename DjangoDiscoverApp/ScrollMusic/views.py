from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def scrollMusic(request):
    return render(request, 'scrollpage.html')

def displayPublication(request):
    return render(request, 'publication.html')