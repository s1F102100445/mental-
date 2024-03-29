from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('index_view/', views.index_view, name='index_view'),
    path('index_view2/', views.index_view2, name='index_view2'),
    path('index_main/', views.index_main, name='index_main'),
    path('index_char/', views.index_char, name='index_char'),
    path('register/', views.register, name='register'),
    path('', views.index_main, name='index_main')
]