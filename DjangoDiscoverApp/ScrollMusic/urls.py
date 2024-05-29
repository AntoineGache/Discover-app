from django.urls import include, path
from . import views

app_name='ScrollPage'
urlpatterns = [
    path('scrollmusic/', views.scrollMusic, name='scrollmusic'),
]