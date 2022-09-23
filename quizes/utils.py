from .models import Quiz, Result
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateQuizes(request, quizes, items):

    page = request.GET.get('page')
    paginator = Paginator(quizes, items)
    try:
        quizes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        quizes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        quizes = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, quizes


def searchQuizes(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    try:
        result = Result.objects.get(user=request.user.profile)
    except Result.DoesNotExist:
        result = None


    quizes = Quiz.objects.distinct().filter(
        Q(user__name__icontains=search_query) |
        Q(title__icontains=search_query) |
        Q(date__icontains=search_query) |
        Q(desc__icontains=search_query) |
        Q(number_of_questions__icontains=search_query
          )
    )
    return quizes, result, search_query

#
# http://127.0.0.1:8000/quizes/cae05871-822c-49a0-8e8c-ad8c971cbf93/create-question/
# def paginateQuestions(request, questionForms, items):
#     page = request.GET.get('page')
#     paginator = Paginator(questionForms, items)
#     try:
#         quizes = paginator.page(page)
#     except PageNotAnInteger:
#         page = 1
#         questionForms = paginator.page(page)
#     except EmptyPage:
#         page = paginator.num_pages
#         questionForms = paginator.page(page)
#
#     leftIndex = (int(page) - 4)
#
#     if leftIndex < 1:
#         leftIndex = 1
#
#     rightIndex = (int(page) + 5)
#
#     if rightIndex > paginator.num_pages:
#         rightIndex = paginator.num_pages + 1
#
#     custom_range = range(leftIndex, rightIndex)
#
#     return custom_range, questionForms