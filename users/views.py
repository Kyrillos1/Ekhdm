from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import Profile, Message
from .forms import CustomUserCreationForm, ProfileForm, MessageForm
from .utils import *
from .decorator import unauthenticated_user
from users.decorator import allowed_users
from django.conf import settings
import datetime
import calendar
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder


@unauthenticated_user
def loginUser(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


@unauthenticated_user
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.success(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {'profiles': profiles, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    # topSkills = profile.skill_set.exclude(description__exact="")
    # otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    # skills = profile.skill_set.all()
    demomethods = profile.demomethod_set.all()

    context = {'profile': profile, 'demomethods': demomethods}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


#
#
# @login_required(login_url='login')
# def createSkill(request):
#     profile = request.user.profile
#     form = SkillForm()
#
#     if request.method == 'POST':
#         form = SkillForm(request.POST)
#         if form.is_valid():
#             skill = form.save(commit=False)
#             skill.owner = profile
#             skill.save()
#             messages.success(request, 'Skill was added successfully!')
#             return redirect('account')
#
#     context = {'form': form}
#     return render(request, 'users/skill_form.html', context)
#
#
# @login_required(login_url='login')
# def updateSkill(request, pk):
#     profile = request.user.profile
#     skill = profile.skill_set.get(id=pk)
#     form = SkillForm(instance=skill)
#
#     if request.method == 'POST':
#         form = SkillForm(request.POST, instance=skill)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Skill was updated successfully!')
#             return redirect('account')
#
#     context = {'form': form}
#     return render(request, 'users/skill_form.html', context)
#
#
# @login_required(login_url='login')
# def deleteSkill(request, pk):
#     profile = request.user.profile
#     skill = profile.skill_set.get(id=pk)
#     if request.method == 'POST':
#         skill.delete()
#         messages.success(request, 'Skill was deleted successfully!')
#         return redirect('account')
#
#     context = {'object': skill}
#     return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'users/message.html', context)


@login_required(login_url='login')
def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return redirect('user-profile', pk=recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message_form.html', context)


RANDOM_VARIABLE = settings.SOME_RANDOM_VARIABLE


# @allowed_users(allowed_roles=['اسرة اعداد خدام'])
def makhdomenList(request,quizId):
    makhdomen, search_query = searchMakhdomen(request)
    custom_range, makhdomen = paginateMakhdomen(request, makhdomen, 6)

    totalWeeks = len(Week.objects.all())
    daysLastWeek = []
    for day in RANDOM_VARIABLE:
        daysLastWeek.append(day)
        if calendar.day_name[datetime.datetime.today().weekday()] == day:
            break

    totalDays = totalWeeks * 7 - 7 + len(daysLastWeek)
    makhdomNotes = []
    notesPercentage = []
    for makhdom in makhdomen:
        notes = makhdom.note_set.all().values_list('am', 'pm', 'read_bible', 'liturgy', 'holy_communion', 'confession',
                                                   'week', 'day')

        total = [0, 0, 0, 0, 0]
        notes = list(notes)
        for note in notes:
            # print(note)
            for i, value in enumerate(note):
                if i == 5: break
                total[i] += value
        fields = ['am', 'pm', 'read_bible', 'liturgy', 'holy_communion']
        note = dict(zip(fields, total))
        for key, value in note.items():
            if key in ['am', 'pm', 'read_bible']:
                note[key] *= 100 / totalDays
            else:
                note[key] *= 100 / totalWeeks
        # print(notes)
        makhdomNotes.append(note)

    context = {'twoLists': zip(makhdomen, makhdomNotes),
               'search_query': search_query,
               'custom_range': custom_range,
               'notes': makhdomNotes
               }
    return render(request, 'users/makhdomen.html', context)
