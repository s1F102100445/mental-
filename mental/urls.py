from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('index_view/', views.index_view, name='index_view'),
    path('index_view2/', views.index_view2, name='index_view2')
]