from django.contrib import admin
from django.urls import path
from . import views
# Здесь все мои URLS!
urlpatterns = [
     path('', views.main, name='main-page'),
    path('top-sellers/', views.top_sellers, name='top-sellers'),
    path('advertisement-post/', views.advertisement_post, name='advertisement-post'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile')
]