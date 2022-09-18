from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from users.decorator import allowed_users
from django.contrib.auth.decorators import login_required
from.utils import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)


# @login_required(login_url="login")/
# class QuizListView(ListView):
#     model = Quiz
#     template_name = 'quizes/quizes.html'
#
#     # @login_required(login_url="login")
#     # @allowed_users(allowed_roles=['MakhdomE3dad'])
#     def dispatch(self, request, *args, **kwargs):
#         return super(IndexView, self).dispatch(request, *args, **kwargs)
#     def get_context_data(self,**kwargs):
#         context = super(QuizListView, self).get_context_data(**kwargs)
#     #     # #
#     #     # # result = get_object_or_404(Result, user=self.request.user.profile)
#     #     # if get_object_or_404(Result, user=self.request.user.profile):
#     #     #     result = get_object_or_404(Result, user=self.request.user.profile)
#     #     #     # context['result'] = Result.objects.get(user = self.request.user.profile)
#     #     #     context['result'] = result
#     #     #     return context
#     #
#         try:
#             context['result'] = Result.objects.get(user=self.request.user.profile)
#         except Result.DoesNotExist:
#             pass
#         return context

@login_required(login_url="login")
@allowed_users(allowed_roles=['MakhdomE3dad'])
def QuizListView(request):
    quizes, result, search_query = searchQuizes(request)
    custom_range, quizes = paginateQuizes(request, quizes, 6)

    return render(request, 'quizes/quizes.html', {'quizes': quizes, 'result': result})


@login_required(login_url="login")
@allowed_users(allowed_roles=['MakhdomE3dad'])
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})


@login_required(login_url="login")
@allowed_users(allowed_roles=['MakhdomE3dad'])
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): [str(q.type), answers]})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


@allowed_users(allowed_roles=['MakhdomE3dad'])
def save_quiz_view(request, pk):
    if is_ajax(request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        user = request.user.profile
        quiz = Quiz.objects.get(pk=pk)

        count = quiz.question_quiz.all().count()
        score = 0
        print(data_.items())
        for ques_text, user_answer in data_.items():
            user_answer_new = user_answer[0].split(",")
            while ("" in user_answer_new):
                user_answer_new.remove("")
            for q in quiz.get_questions():
                if q.text == ques_text:
                    if q.type == 'mcq':
                        answers = []
                        for a in q.get_answers():
                            if a.correct == True: answers.append(a.text)
                        answers.sort()
                        user_answer_new.sort()
                        print(answers)
                        print(user_answer_new)
                        if answers == user_answer_new:
                            score += q.grade
                    # else :
                    # print(user_answer)
                    userAns = UserAns()
                    userAns.question = q
                    userAns.user = request.user.profile
                    userAns.text = str(user_answer)
                    userAns.save()

        result, created = Result.objects.get_or_create(quiz=quiz, user=user)
        if created:
            result.score = score
            result.save()
        return JsonResponse({'done': True})
