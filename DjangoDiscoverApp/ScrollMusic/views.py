from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def scrollMusic(request):
    html = "<html><body>Scroll Music</body></html>"
    return HttpResponse(html)