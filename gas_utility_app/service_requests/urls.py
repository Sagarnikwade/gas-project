from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_request, name='new_request'),
    path('', views.request_list, name='request_list'),
    path('<int:pk>/', views.request_detail, name='request_detail'),
]
