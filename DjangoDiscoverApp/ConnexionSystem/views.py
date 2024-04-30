from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def signIn(request):    
    return render(request, 'signin/signin.html')

def signOut(requst):
    html = "<html><body>sigOut</body></html>"
    return HttpResponse(html)

def register(request):
    return render(request, 'register/register.html')