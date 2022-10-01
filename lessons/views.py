from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import LessonForm
from reacts.forms import CommentForm
from reacts.models import Like
from .utils import searchLessons, paginateLessons


def lessons(request, type):
    lessonType = LessonType.objects.get(id=type)
    lessons, search_query = searchLessons(request, lessonType)
    custom_range, lessons = paginateLessons(request, lessons, 6)
    form = CommentForm()
    context = {'lessons': lessons,
               'search_query': search_query,
               'custom_range': custom_range,
               'form': form,
               'lessonType': lessonType
               }
    return render(request, 'lessons/lessons.html', context)


def lesson(request, type, slug):
    lessonType = LessonType.objects.get(id=type)
    context = {}
    try:
        lesson = lessonType.lesson_set.filter(slug=slug).first()
        form = CommentForm()
        print(lesson)
        context = {
            'lesson': lesson,
            'form': form,
        }
    except Exception as e:
        print(e)
    return render(request, 'lessons/single_lesson.html', context)


@login_required(login_url="login")
def create_lesson(request, type):
    context = {'form': LessonForm}
    lessonType = LessonType.objects.get(id=type)
    try:
        if request.method == 'POST':
            form = LessonForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user.profile

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            lesson = Lesson.objects.create(
                user=user, title=title,
                content=content, type=lessonType, image = image, public=True
            )
            print(lesson)
            return redirect('lessons')
    except Exception as e:
        print(e)

    return render(request, "lessons/lesson_form.html", context)



@login_required(login_url="login")
def update_lesson(request, type, slug):
    context = {}
    try:
        lessonType = LessonType.objects.get(id=type)
        lesson = lessonType.lesson_set.get(slug=slug)

        if lesson.user != request.user:
            return redirect('lessons/')

        initial_dict = {'content': lesson.content}
        form = LessonForm(initial=initial_dict)
        if request.method == 'POST':
            form = LessonForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user.profile

            if form.is_valid():
                content = form.cleaned_data['content']

            lesson = Lesson.create(
                user=user, title=title,
                content=content, image=image, type=lessonType
            )

        context['lesson'] = lesson
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'lessons/lesson_form.html', context)


@login_required(login_url="login")
def delete_lesson(request, pk):
        try:
            lesson = Lesson.objects.get(id=pk)

            if lesson.user == request.user.profile:
                lesson.delete()

        except Exception as e:
            print(e)

        return redirect('lessons')
