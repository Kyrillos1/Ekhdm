from django.urls import path
from . import views
from django.views.static import serve
#from django.conf.urls import url
from reacts.views import *
urlpatterns = [
    path('comment/<str:pk>/<str:model>/', comment, name="comment"),
    path('comments/<str:pk>/<str:model>/', comments, name="comments"),
    path('like/<str:pk>/<str:model>/', like, name='like'),
    path('likes/<str:pk>/<str:model>/', likes, name='likes'),

]