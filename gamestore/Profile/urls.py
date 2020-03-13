from . import views
from django.urls import path

urlpatterns = [
    path('myGame/', views.myGame, name='myGame'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('logout/', views.logouted, name='logout'),
    path('buy/<int:id>', views.buy, name='buy'),
]