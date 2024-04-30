from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def signIn(request):
    html = "<html><body>sigIn</body></html>"
    return HttpResponse(html)

def signOut(requst):
    html = "<html><body>sigOut</body></html>"
    return HttpResponse(html)

def register(request):
    html = "<html><body>Register</body></html>"
    return HttpResponse(html)