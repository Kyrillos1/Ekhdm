from django.urls import path
from . import views

urlpatterns = [
    path('', views.demomethods, name="demomethods"),
    path('demomethod/<str:pk>/', views.demomethod, name="demomethod"),

    path('create-demomethod/', views.createDemomethod, name="create-demomethod"),

    path('update-demomethod/<str:pk>/', views.updateDemomethod, name="update-demomethod"),

    path('delete-demomethod/<str:pk>/', views.deleteDemomethod, name="delete-demomethod"),
]
