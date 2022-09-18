from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('demomethods/', views.getDemomethods),
    path('demomethods/<str:pk>/', views.getDemomethod),
    path('demomethods/<str:pk>/vote/', views.demomethodVote),

    path('remove-tag/', views.removeTag)
]
