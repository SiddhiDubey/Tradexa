from django.urls import path
from . import views
from django.contrib.auth import login, views as auth_views

urlpatterns = [
    path('', views.app1, name="app1"),
    path('register/', views.registerPage, name="registerPage"),
    path('create_post/', views.postPage, name="postPage"),
    path('login/', views.loginPage, name='loginPage'),

]


