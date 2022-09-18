from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name="tasks"),
    path('task/<str:pk>/', views.task, name="task"),
    path('create-task/', views.createTask, name="create-task"),
    path('submit-task/<str:pk>/', views.submitTask, name="submit-task"),
    path('view-submits/<str:pk>/', views.viewSubmits, name="view-submits"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
]