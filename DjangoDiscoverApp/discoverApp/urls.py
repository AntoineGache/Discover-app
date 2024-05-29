from django.urls import include, path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('parameters/', views.parameters, name='parameters'),
    path('notifications/', views.notifications, name='notifications')
]