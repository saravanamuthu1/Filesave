from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Homeview.as_view(),name='homepage'),
    path('login/',views.Loginview.as_view(),name='loginpage'),
    path('<str:user_name>/upload',views.Uploadview.as_view(),name='uploadpage'),
    path('logout/',views.Logoutview.as_view(),name='logoutpage'),
]