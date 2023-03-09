from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('', views.hello),
    path('hello/<str:username>', views.hello), #variable string en la url
    path('projects/', views.projects),
    path('task/', views.task, name="tasks"),

]