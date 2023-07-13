from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile')
]