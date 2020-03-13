from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('catagory/', views.category, name='catagory'),
]