from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.logined, name='login'),
    path('register/', views.register, name='register'),
]