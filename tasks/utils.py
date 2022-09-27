from .models import Task
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateTasks(request, tasks, results):

    page = request.GET.get('page')
    paginator = Paginator(tasks, results)

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        tasks = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        tasks = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, tasks


def searchTasks(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # tags = Tag.objects.filter(name__icontains=search_query)

    tasks = Task.objects.distinct().filter(
        Q(level__in=request.user.profile.get_levels()) &
        (
                Q(desc__icontains=search_query) |
                Q(subject__icontains=search_query) |
                Q(deadline__icontains=search_query) |
                Q(user__name__icontains=search_query)
        )

    )
    return tasks, search_query
