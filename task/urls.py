from django.urls import path
from . import views

urlpatterns = [
    path('', views.task, name='task'),
    path('get/', views.task_get, name='task_get'),
    path('post/', views.task_post, name='task_post'),
]
