from django.urls import path
from . import views
from django.contrib.auth import authenticate, login

    

urlpatterns = [
    path('', views.register, name='register'),
    path('/login', views.user_login, name='login'),
    path('/mypage', views.mypage, name='mypage'),
    path('/wrong', views.wrong, name='worng')
]