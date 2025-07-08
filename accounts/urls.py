from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.auth_login, name='login'),
    path('logout/', views.auth_logout, name='logout'),
    path('register/', views.register, name='register'),
]
