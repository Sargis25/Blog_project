from django.urls import path
from . import views
    

urlpatterns = [
    path('', views.main, name='main'),
    path('newpost/', views.index, name='newpost'),
    path('show/', views.show, name='show'),
    path('thanks/', views.thanks, name='thanks'),
]