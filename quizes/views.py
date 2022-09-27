from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

# from easy_pdf.rendering import render_to_pdf_response
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.shortcuts import get_object_or_404
from users.decorator import allowed_users
from django.contrib.auth.decorators import login_required
from .utils import *
from .forms import *
import json
from django.core import serializers
from quizes.templatetags.filter import *
import random
from users.models import Profile
from django.db.models import Sum
from django.contrib import messages




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
#     # @allowed_users(allowed_roles=['اسرة اعداد خدام - مخدومين'])
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


# for listing quizes
@login_required(login_url="login")
@allowed_users(allowed_roles=['اسرة اعداد خدام - مخدومين'])
def QuizListView(request):
    quizes, result, search_query = searchQuizes(request)
    custom_range, quizes = paginateQuizes(request, quizes, 6)

    return render(request, 'quizes/quizes.html', {'quizes': quizes, 'result': result})


# for quiz's questions
@login_required(login_url="login")
@allowed_users(allowed_roles=['اسرة اعداد خدام - مخدومين'])
def quiz_view(request, pk):
    quiz = Quiz.objects.get(id=pk)
    user = request.user.profile
    result, created = Result.objects.get_or_create(
        user=user,
        quiz=quiz,
    )
    result.save()

    questions = quiz.question_quiz.all()

    # shuffle questions
    random.seed(request.user.id)
    questions = sorted(questions[:10], key=lambda x: random.random())

    custom_range, questions = paginateQuizes(request, questions, 1)
    try:
        userAnswer = UserAns.objects.get(user=user, question=questions[0]).text
    except:
        userAnswer = ''
    # print()
    quiz = Quiz.objects.filter(id=pk).values('id', 'title', 'date', 'time', 'desc', 'number_of_questions')[0]
    print(userAnswer)
    return render(request, 'quizes/quiz.html',
                  {
                      'quiz': quiz,
                      'questions': questions,
                      'custom_range': custom_range,
                      'userAnswer': userAnswer
                  })


# for saving answers
@login_required(login_url="login")
@allowed_users(allowed_roles=['اسرة اعداد خدام - مخدومين'])
def save_quiz_view(request, pk):
    if is_ajax(request):
        data = request.POST

        data_ = dict(data)
        data_.pop('csrfmiddlewaretoken')
        print(data_)
        question = Question.objects.get(id=data_['id'][0])
        user = request.user.profile
        try:
            userAns = UserAns.objects.get(user=user, question=question)
            if question.type == 'mcq':
                try:
                    userAns.text = data_['ansMcq[]']
                except:
                    userAns.text = None
            elif question.type == 'written':
                userAns.text = data_['ansWritten'][0]
                # print(data_['ansWritten'])
                # print(data_['ansWritten'])
            userAns.save()
        except:
            userAns = UserAns()
            userAns.user = user
            userAns.question = question
            if question.type == 'mcq':
                try:
                    userAns.text = data_['ansMcq[]']
                except:
                    userAns.text = None
            elif question.type == 'written':
                userAns.text = data_['ansWritten'][0]
            userAns.save()

        # quiz = Quiz.objects.get(pk=pk)
        #
        # count = quiz.question_quiz.all().count()
        # score = 0
        # print(data_.items())
        # for ques_text, user_answer in data_.items():
        #     user_answer_new = user_answer[0].split(",")
        #     while ("" in user_answer_new):
        #         user_answer_new.remove("")
        #     for q in quiz.get_questions():
        #         if q.text == ques_text:
        #             if q.type == 'mcq':
        #                 answers = []
        #                 for a in q.get_answers():
        #                     if a.correct == True: answers.append(a.text)
        #                 answers.sort()
        #                 user_answer_new.sort()
        #                 print(answers)
        #                 print(user_answer_new)
        #                 if answers == user_answer_new:
        #                     score += q.grade
        #             # else :
        #             # print(user_answer)
        #             userAns = UserAns()
        #             userAns.question = q
        #             userAns.user = request.user.profile
        #             userAns.text = str(user_answer)
        #             userAns.save()
        #
        # result, created = Result.objects.get_or_create(quiz=quiz, user=user)
        # if created:
        #     result.score = score
        #     result.save()
        return JsonResponse({'done': True})


@allowed_users(allowed_roles=['اسرة اعداد خدام'])
@login_required(login_url="login")
def manageQuizes(request):
    quizes, result, search_query = searchQuizes(request)
    custom_range, quizes = paginateQuizes(request, quizes, 6)
    user = request.user.profile
    admitor = UserAns.objects
    makhdomen = Profile.objects.filter()


    # submit=[]
    context = {
        # 'twolists': twolists,
        'quizes': quizes,
        'search_query': search_query,
        'custom_range': custom_range,
        'makhdomen': makhdomen,


        # 'form': form,
    }

    return render(request, 'quizes/manage_quizes.html', context)


@allowed_users(allowed_roles=['اسرة اعداد خدام'])
@login_required(login_url="login")
def createQuiz(request, pk=None):
    profile = request.user.profile

    try:
        quiz = Quiz.objects.get(id=pk)
        form = QuizForm(instance=quiz)
    except:
        quiz = ''
        form = QuizForm()
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        try:
            form = QuizForm(request.POST, request.FILES, instance=quiz)
            if form.is_valid():
                quiz = form.save()
                quiz.save()
        except:
            if form.is_valid():
                quiz = form.save(commit=False)
                quiz.user = profile
                quiz.save()
        return redirect('manage-quizes')
    context = {'quizForm': form}
    return render(request, "quizes/quiz_form.html", context)


@allowed_users(allowed_roles=['اسرة اعداد خدام'])
@login_required(login_url="login")
def createQuestion(request, pk, pk2):
    profile = request.user.profile
    quiz = Quiz.objects.get(id=pk)

    questionForm = QuestionForm()
    try:
        question = Question.objects.get(id=pk2)
        questionForm = QuestionForm(instance=question)
    except:
        question = ''

    if request.method == 'POST':
        print(request.POST)
        questionForm = QuestionForm(request.POST, request.FILES)
        try:
            questionForm = QuestionForm(request.POST, request.FILES, instance=question)
            if questionForm.is_valid():
                question = questionForm.save()
                question.save()
                return redirect('manage-quizes')
        except:
            if questionForm.is_valid():
                question = questionForm.save(commit=False)
                question.user = profile
                question.quiz = quiz
                question.save()
                return redirect('manage-quizes')
    context = {
        'questionForm': questionForm,
        # 'answerForm': answerForm,
    }
    return render(request, "quizes/question_form.html", context)


@allowed_users(allowed_roles=['اسرة اعداد خدام'])
@login_required(login_url="login")
def remarkQuiz(request, quiz_pk, user_pk):
    quiz = Quiz.objects.get(id=quiz_pk)
    user = Profile.objects.get(id=user_pk)
    totalGrades = Question.objects.filter(quiz=quiz).aggregate(Sum('grade'))
    print(totalGrades)
    mcqAnwsers = UserAns.objects.filter(user=user, question__quiz=quiz, question__type='mcq')
    anwsers = []
    for mcqAnwser in mcqAnwsers:
        if mcqAnwser.text != None:

            anwsers = mcqAnwser.text.strip("[']").split("', '")

            anwsers.sort()
            correctAnwsers = mcqAnwser.question.correctAnswers.split(",")
            correctAnwsers.sort()
            if anwsers == correctAnwsers:
                mcqAnwser.grade = mcqAnwser.question.grade
                mcqAnwser.save()
    writtenAnwsers = UserAns.objects.filter(user=user, question__quiz=quiz, question__type='written')
    if writtenAnwsers:
        if request.method == 'POST':
            data = dict(request.POST)
            data.pop('csrfmiddlewaretoken')
            for writtenAnwser, value in zip(writtenAnwsers, data.values()):
                writtenAnwser.grade = value[0]
                writtenAnwser.save()

            allAnwsers = UserAns.objects.filter(user=user, question__quiz=quiz).aggregate(Sum('grade'))
            try:
                result = Result.objects.filter(user=user, quiz=quiz)[0]
            except:
                result = Result()
                result.quiz = quiz
                result.user = user
                result.score = allAnwsers['grade__sum']*100/totalGrades['grade__sum']
            result.score = allAnwsers['grade__sum']*100/totalGrades['grade__sum']
            result.completed = True
            result.save()
            messages.success(request, user.name + "'s answer was remarked")
            return redirect('manage-quizes')
        return render(request, "quizes/remark-quiz.html", {'writtenAnwsers': writtenAnwsers, 'user': user})
    else:
        allAnwsers = UserAns.objects.filter(user=user, question__quiz=quiz).aggregate(Sum('grade'))
        try:
            result = Result.objects.filter(user=user, quiz=quiz)[0]
        except:
            result = Result()
            result.quiz = quiz
            result.user = user
            result.score = allAnwsers['grade__sum']*100/totalGrades['grade__sum']

        result.score = allAnwsers['grade__sum']*100/totalGrades['grade__sum']
        result.completed = True
        result.save()
        messages.success(request, user.name+"'s answer was remarked")
        return redirect('manage-quizes')

# def  venue_pdf(request, quiz_pk, user_pk):
#     buf = io.BytesIO()
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     textob = c.beginText()
#     textob.setTextOrigin(inch,inch)
#     textob.setFont('Helvetica', 14)
#     for line in lines:
#         textob.textLine(line)
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename='venue.pdf')

def result_pdf(request, quiz_pk, user_pk):
    quiz = Quiz.objects.get(id=quiz_pk)
    user = Profile.objects.get(id=user_pk)
    answers = UserAns.objects.filter(user=user, question__quiz=quiz)
    result = Result.objects.filter(user=user, quiz=quiz)[0]
    context = {
        'answers': answers,
        'result': result,
    }
    template_path = 'quizes/result_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="quiz_result_'+user.name+'_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return render(request, template_path, context)


def result_view(request, quiz_pk, user_pk):
    quiz = Quiz.objects.get(id=quiz_pk)
    user = Profile.objects.get(id=user_pk)
    answers = UserAns.objects.filter(user=user, question__quiz=quiz)
    result = Result.objects.filter(user=user, quiz=quiz)[0]
    context = {
        'answers': answers,
        'result': result,
    }
    template_path = 'quizes/result_view.html'
    return render(request, template_path, context)



# def manageQuiz(request, pk):
#     quiz = Quiz.objects.get(id=pk)
#     questions = quiz.get_questions()
#     custom_range, questions = paginateQuizes(request, questions, 6)
#     # print(questions)
#     # questionsjson = json.simplejson.dumps(questions)
#     q = serializers.serialize('json', questions)
#     print(q)
#     return HttpResponse(q, content_type='application/json')

# for q in questions:
#     answers = []
#     for a in q.get_answers():
#         answers.append(a.text)
# #     questions.append({str(q): [str(q.type), answers]})
#
#
# return JsonResponse({
#         'data': 'h',
#     })

# @login_required(login_url="login")
# def createQuestions(request, pk):
#     profile = request.user.profile
#     context = {
#         'questionForms': questionForms,
#         # 'quizForm': quizForm,
#     }
#     return render(request, "quizes/quiz_form.html", context)


# @login_required(login_url="login")
# def createQuestions(request, pk):
#     profile = request.user.profile
# if pk != None:
#     quizForm = QuizForm(instance=Quiz.objects.get(id=pk))
# quiz = Quiz.objects.get(id=pk)
# numberOfQuestions=quiz.number_of_questions
# print(numberOfQuestions)
# questionForms=[]
# for i in range(numberOfQuestions):
#     questionForm = QuestionForm()
#     questionForms.append(questionForm)
# custom_range, questionForms = paginateQuizes(request, questionForms, 1)
# for questionForm in questionForms:
# if request.POST:
# form = QuestionForm()
# if pk != None:
# print('false')
#     form = QuizForm(instance=Quiz.objects.get(id=pk))
# if request.method == 'POST':
# print('true')
# form = QuestionForm(request.POST, request.FILES)
# print(form)
# if form.is_valid():
#     question = form.save(commit=False)
#     question.user = profile
#     question.quiz = quiz
#     question.save()

# print(page)
# if :
#     submit = Submit.objects.filter(user=profile,task=task)[0]
#     form = SubmitForm(instance=submit)
# except:
#     pass
# if request.method == 'POST':
#     form = QuestionForm(request.POST, request.FILES)
#     if form.is_valid():
#         question = form.save(commit=False)
#         question.user = profile
#         question.save()

# return redirect('quizes')
#
# context = {
#     'questionForms': questionForms,
#     # 'quizForm': quizForm,
# }
# return render(request, "quizes/quiz_form.html", context)
