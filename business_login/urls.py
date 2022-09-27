from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('reservation_list', views.reservation_list, name='reservation_list'),
]
