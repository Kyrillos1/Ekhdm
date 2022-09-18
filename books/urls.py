from django.urls import path
from . import views
from django.views.static import serve
#from django.conf.urls import url

urlpatterns = [
    path('', views.books, name="books"),
    path('book/<str:pk>/', views.book, name="book"),
    path('create-book/', views.createBook, name="create-book"),
    path('update-book/<str:pk>/', views.updateBook, name="update-book"),
    path('delete-book/<str:pk>/', views.deleteBook, name="delete-book"),
    #url(r'^download/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]