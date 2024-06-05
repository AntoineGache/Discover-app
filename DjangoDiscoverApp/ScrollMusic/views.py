from django.shortcuts import render
from django.http import HttpResponse
from discoverApp.models import Publication


# Create your views here.

def scrollMusic(request):
    return render(request, 'postfeed/postfeed.html')

def displayPublication(request):
    return render(request, 'publication.html')

def publications_view(request):
    publications = Publication.objects.all()
    return render(request, 'publication.html', {'publications': publications})
