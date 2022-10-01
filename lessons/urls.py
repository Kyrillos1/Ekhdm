from django.urls import path
from .views import *

urlpatterns = [
    path('<str:type>/', lessons, name="lessons"),

    path('<str:type>/lesson/<str:slug>/', lesson, name="lesson"),

    path('<str:type>/create-lesson/', create_lesson, name="create-lesson"),

    path('<str:type>/update-lesson/<str:slug>/', update_lesson, name="update-lesson"),

    path('<str:type>/delete-lesson/<str:slug>/', delete_lesson, name="delete-lesson"),
]