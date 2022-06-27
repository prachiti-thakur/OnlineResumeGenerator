
from django.contrib import admin
from django.urls import path
from UserApp import views

urlpatterns = [
    path('',views.home),
    path('signup',views.signup),
    path('login',views.login),
    path('logout',views.logout),
    path('personal_info',views.personal_information),
    #path('fields',views.fields),
    path('educational_Details/<Pers>',views.educational_Details)
]
