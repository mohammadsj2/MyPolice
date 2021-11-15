from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('signout/', views.signout, name='home'),
]
