from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from weeks.models import *
from .forms import NoteForm
from django.contrib import messages
from django.conf import settings
import datetime
import calendar
from users.decorator import allowed_users
from django.contrib.auth.decorators import login_required


RANDOM_VARIABLE = settings.SOME_RANDOM_VARIABLE

@login_required(login_url="login")
@allowed_users(allowed_roles=['اسرة اعداد خدام - مخدومين'])
def note(request):
    user = request.user.profile
    last_week = Week.objects.first()
    form = NoteForm()
    days=[]
    for day in RANDOM_VARIABLE:
        days.append(day)
        if calendar.day_name[datetime.datetime.today().weekday()] == day:
            break
    if request.method == 'POST':
        print(request.POST)
        form = NoteForm(request.POST)
        if form.is_valid():
            note, created = Note.objects.get_or_create(
                week=last_week,
                day=request.POST.get('day'),
            )
            if created:
                note.week = last_week
                note.user = request.user.profile
                note.save()
                messages.success(request, 'Note added')
    return render(request, 'notes/note_form.html', {'form': form, 'days': days})
