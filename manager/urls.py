from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('signout/', views.sign_out, name='home'),
    path('create_police/', views.create_police, name='create_police'),
    path('create_mission/', views.create_mission, name='create_mission'),
    path('policemen_profile/<str:username>', views.policemen_profile, name='policemen_profile_username'),
    path('policemen_list/', views.policemen_list, name='policemen_list'),
    path('mission_profile/<int:mission_id>', views.mission_profile, name='mission_profile'),
    path('mission_profile/<int:mission_id>/end_mission', views.end_mission, name='end_mission'),
    path('mission_list/', views.mission_list, name='mission_list')
]
