from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about),
    path("student",views.student),
    path("contact",views.contact),
    path("teacher",views.teacher),
]