from django.db.models import Q
from .models import Profile

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from weeks.models import *
from notes.models import *

def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query)
        # Q(skill__in=skills)
    )

    return profiles, search_query


def paginateMakhdomen(request, makhdomen, results):
    page = request.GET.get('page')
    paginator = Paginator(makhdomen, results)

    try:
        makhdomen = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        makhdomen = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        makhdomen = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, makhdomen


def searchMakhdomen(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    makhdomen = Profile.objects.filter(
        Q(user__groups__name='MakhdomE3dad')&
        (
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(username__icontains=search_query) |
            Q(social_facebook__icontains=search_query) |
            Q(job__icontains=search_query)
        )
    )


    return makhdomen, search_query
