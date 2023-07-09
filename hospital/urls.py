from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('createaccount/', views.createaccountpage, name='createaccountpage'),
    path('login', views.loginpage, name='loginpage'),
    path('logout/', views.logout, name='logout'),
    path('login_admin', views.login_admin, name='login_admin')
]
