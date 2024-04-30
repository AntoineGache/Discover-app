from django.urls import include, path
from .login import *

urlpatterns = [
    path("login/", include(extra_patterns)),
]
