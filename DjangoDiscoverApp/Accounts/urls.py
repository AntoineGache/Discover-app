from django.urls import include, path
from . import views

app_name="Account"
urlpatterns = [
    path('accounts/', views.accounts, name='account'),
]