from django.urls import path
from . import views

# Installed apps 
urlpatterns = [
    path('register/', views.user_reg, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]