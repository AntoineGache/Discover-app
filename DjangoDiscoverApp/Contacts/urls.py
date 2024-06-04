from django.urls import include, path
from . import views

app_name="Contact"
urlpatterns = [
    path('contactpage/', views.contact, name='contactPage'),
    path('getmessage/', views.getMessage, name='getMessage'),
]