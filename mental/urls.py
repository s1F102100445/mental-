from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_view/', views.index_view, name='index_view'),
]