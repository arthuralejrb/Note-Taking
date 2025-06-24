"""Define URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    # login page
    path('login/', LoginView.as_view(), {'template_name': 'users/templates/registration/login.html'},
         name = 'login'),
    
    # log out page
    path('logout/', views.logout_view, name='logout'),
    
    # Register page
    path('register/', views.register, name='register'),
]