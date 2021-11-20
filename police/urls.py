from django.urls import path

from . import views

# This file manages police urls

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('signout/', views.sign_out, name='home'),
    path('mission/', views.mission, name='mission'),
    path('notifications/', views.notifications, name='notifications')
]