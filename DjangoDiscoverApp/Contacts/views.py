from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(request):
    html = "<html><body>Contact</body></html>"
    return HttpResponse(html)