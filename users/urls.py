from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('logout/', views.c_logout, name='logout'),
    # path('login/', views.c_login, name='login'),
    path('register/', views.register, name='register'),
]
