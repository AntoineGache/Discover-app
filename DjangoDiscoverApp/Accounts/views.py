from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def accounts(request):
    html = "<html><body>Accounts</body></html>"
    return HttpResponse(html)