from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('studenti/', views.list_students,name="list-student"),
    path('ucitelia/', views.list_teachers,name="list-student"),
    path('triedy/', views.list_class,name="list-trieda"),
]
