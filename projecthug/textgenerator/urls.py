from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_text, name='generate_text'),
    path('result/', views.result, name='result'),
    path('index/', views.index, name='index'),
]
