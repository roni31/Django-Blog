from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('login/',views.login),
    path('addblog/',views.addblog),
    path('home/',views.home),

]

# 127.0.0.1:8000/