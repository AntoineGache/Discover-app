from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/', views.accounts, name='accounts'),
]