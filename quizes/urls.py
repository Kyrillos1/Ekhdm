from django.urls import path
from users.decorator import allowed_users
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
#path('create-quiz/<str:pk>/question/<str:pk2>/', createQuestion, name="create-question"),
#path('manage-quizes/<str:pk>/', manageQuiz, name="manage-quiz"),
#path('', QuizListView.as_view(), name='main_view'),

path('manage-quizes/', manageQuizes, name="manage-quizes"),
path('create-quiz/<str:pk>/', createQuiz, name="create-quiz"),
path('create-quiz/<str:pk>/question/<str:pk2>', createQuestion, name="create-question"),
path('remark-quiz/<str:quiz_pk>/<str:user_pk>/', remarkQuiz, name="remark-quiz"),
#path('venue_pdf/<str:quiz_pk>/<str:user_pk>/', venue_pdf, name="venue_pdf"),
path('result_pdf/<str:quiz_pk>/<str:user_pk>/', result_pdf, name="result_pdf"),
path('result_view/<str:quiz_pk>/<str:user_pk>/', result_view, name="result_view"),

path('', QuizListView, name='main_view'),
path('<pk>/', quiz_view, name='quiz_view'),
path('<pk>/save/', save_quiz_view, name='save-view'),




]
