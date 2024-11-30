from django.urls import path
from django.contrib.auth.views import LoginView  # Import LoginView from Django auth
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(), name='login'),  # Use Django's built-in LoginView
]
