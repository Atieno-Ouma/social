from django.urls import path,re_path,include
from . import views

urlpatterns = [

    path('home/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('settings/', views.settings, name='settings'),
    path('logout/', views.logout, name='logout'),



]