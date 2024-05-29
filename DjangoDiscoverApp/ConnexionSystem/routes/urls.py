from django.urls import include, path
from .login import *

app_name="ConnexionSystem"
urlpatterns = [
    path("login/", include(extra_patterns)),
]
