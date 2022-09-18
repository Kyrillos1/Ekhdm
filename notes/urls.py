from django.urls import path
from . import views

urlpatterns = [
    #path('add_note', views.tasks, name="tasks"),
    path('add_note/', views.note, name="note"),
    #path('create-task/', views.createTask, name="create-task"),
    #path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
]
