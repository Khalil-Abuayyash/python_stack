from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('success', views.show_user_page),
    path('logout', views.logout)
]