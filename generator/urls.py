from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('password/', views.password),
    path('about/', views.about),
]