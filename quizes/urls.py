from django.urls import path
from users.decorator import allowed_users
from django.contrib.auth.decorators import login_required
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

urlpatterns = [
#path('', QuizListView.as_view(), name='main_view'),
path('', QuizListView, name='main_view'),
path('<pk>/', quiz_view, name='quiz_view'),
path('<pk>/save/', save_quiz_view, name='save-view'),
path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]
