from django.urls import include, path
from . import views

app_name='ScrollPage'
urlpatterns = [
    path('scrollmusic/', views.scrollMusic, name='scrollmusic'),
    path('publications/', views.publications_view, name='publications'),

]