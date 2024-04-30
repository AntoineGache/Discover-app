from django.urls import path
from .. import views

extra_patterns = [
    path('signin/', views.signIn, name='signin'),
    path('register/', views.register, name='register'),
    path('signout/', views.signOut, name='signout'),
]