from django.urls import path

from . import views

app_name = 'predictBP'
urlpatterns = [
    path('', views.index, name='index'),
    path('matrix', views.matrix, name='matrix'),
    path('modul', views.modul, name='matrix'),
]