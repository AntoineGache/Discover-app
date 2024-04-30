from django.urls import include, path
from . import views

urlpatterns = [
    path('scrollmusic/', views.scrollMusic, name='scrollmusic'),
]