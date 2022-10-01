from .models import Lesson
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateLessons(request, lessons, results):
    page = request.GET.get('page')
    paginator = Paginator(lessons, results)

    try:
        lessons = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        lessons = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        lessons = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, lessons


def searchLessons(request,lessonType):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # tags = Tag.objects.filter(name__icontains=search_query)

    lessons = lessonType.lesson_set.distinct().filter(
        (
            Q(public=True)
            # Q(level__in=request.user.profile.get_levels())
        ) &
        (
                Q(title__icontains=search_query) |
                Q(user__name__icontains=search_query)
        )
    )
    return lessons, search_query
