from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from reacts.forms import CommentForm
from .utils import searchTasks, paginateTasks
from users.decorator import allowed_users
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)

@login_required(login_url="login")
def tasks(request):
    tasks, search_query = searchTasks(request)
    custom_range, tasks = paginateTasks(request, tasks, 6)
    user = request.user.profile
    # submit=[]
    context = {
        # 'twolists': twolists,
                'tasks':tasks,
               'search_query': search_query,
               'custom_range': custom_range,
               # 'form': form,
               }

    return render(request, 'tasks/tasks.html', context)


@login_required(login_url="login")
def task(request, pk):
    taskObj = Task.objects.get(id=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.task = taskObj
        comment.user = request.user.profile
        comment.save()

        messages.success(request, 'Your comment was successfully submitted!')
        return redirect('task', pk=taskObj.id)

    return render(request, 'tasks/single-task.html', {'task': taskObj, 'form': form})


@allowed_users(allowed_roles=['اسرة اعداد خدام'])
@login_required(login_url="login")
def createTask(request):
    profile = request.user.profile
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = profile
            task.save()

            return redirect('tasks')

    context = {'form': form}
    return render(request, "tasks/task_form.html", context)


@allowed_users(allowed_roles=['اسرة اعداد خدام'])
@login_required(login_url="login")
def deleteTask(request, pk):
    profile = request.user.profile
    task = profile.task_set.get(id=pk)
    if task:
        if request.method == 'POST':
            task.delete()
            return redirect('tasks')

    context = {'object': task}
    return render(request, 'delete_template.html', context)


# @allowed_users(allowed_roles=['اسرة اعداد خدام'])
@login_required(login_url="login")
def submitTask(request, pk):
    profile = request.user.profile
    form = SubmitForm()
    task = Task.objects.get(id=pk)
    try:
        submit = Submit.objects.filter(user=profile,task=task)[0]
        form = SubmitForm(instance=submit)
    except:
        pass

    if request.method == 'POST':
        form = SubmitForm(request.POST, request.FILES)
        try:
            form = SubmitForm(request.POST, request.FILES, instance=submit)
            if form.is_valid():
                submit =form.save()
                submit.save()

        except:
            if form.is_valid():
                submit = form.save(commit=False)
                submit.user = profile
                submit.task = Task.objects.get(id=pk)
                submit.save()

        return redirect('tasks')

    context = {'form': form}
    return render(request, 'tasks/submit-form.html', context)

@login_required(login_url="login")
def viewSubmits(request, pk):

    submit = Submit.objects.get(id=pk)
    context = {'submit': submit}
    return render(request, 'tasks/view-submits.html', context)