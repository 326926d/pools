from django.urls import path
from pool import views


urlpatterns = [
    path("", views.index, name="index"),
    path('add', views.add, name = 'add'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('signout/', views.signout, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('create/', views.create),
    path('user_register/', views.user_register, name='user_register'),
    path('home_view/', views.home_view, name='home_view'), 
    path('get_name/', views.get_name, name='get_name'),
]