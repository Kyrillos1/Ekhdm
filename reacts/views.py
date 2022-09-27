from django.shortcuts import render
from .models import *
from .forms import *
from django.http import JsonResponse, HttpResponse
from books.models import Book
from django.core import serializers
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.core import serializers

# from django import template
# from django.template.loader import get_template
# from django import Context

# Create your views here.
def comment(request,pk,model):
    data = request.POST
    form = CommentForm(request.POST)
    comment = form.save(commit=False)
    comment.user = request.user.profile
    if model == 'book':
        obj = Book.objects.get(id=pk)
        comment.book = obj
    if model == 'post':
        obj = Post.objects.get(id=pk)
        comment.post = obj
    comment.save()

    return JsonResponse({'done': True})


def comments(request,pk, model):

    comments = Comment.objects.filter(
        Q(book=pk) |
        Q(post=pk) |
        Q(task=pk)
    )
    context = {'comments': comments}
    return render(request, 'reacts/comments.html', context)

@login_required
def like(request,pk, model):
    print(pk)
    user = request.user.profile
    like = Like.objects.filter(
        Q(user=user) &
        (
                Q(book=pk) |
                Q(post=pk) |
                Q(task=pk)
        )
    )
    if like:
        like.delete()
        button = 'Like'
    else:
        like = Like()
        like.user = user
        if model == 'book':
            obj = Book.objects.get(id=pk)
            like.book = obj
        if model == 'post':
            obj = Post.objects.get(id=pk)
            like.post = obj
        if model == 'task':
            obj = Task.objects.get(id=pk)
            like.post = obj
        like.save()
        button = 'Dislike'
    return JsonResponse({
        'button': button,
    })

@login_required
def likes(request, pk, model):
    user = request.user.profile
    like = Like.objects.filter(
        Q(user=user) &
        (
                Q(book=pk) |
                Q(post=pk) |
                Q(task=pk)
        )
    )
    if like:
        button = 'Like'
    else:
        button = 'Dislike'
    return JsonResponse({
        'button': button,
    })
    # profile = request.user.profile
    # if request.method == 'POST':
    #     post_id = request.POST.get('post_id')
    #     post = Post.objects.get(id=post_id)
    #
    #     if profile in post.liked.all():
    #         post.liked.remove(profile)
    #     else:
    #         post.liked.add(profile)
    #
    #     like, created = Like.objects.get_or_create(user=profile, post=post)
    #
    #     if not created:
    #         if like.value == 'Like':
    #             like.value = 'Unlike'
    #         else:
    #             like.value = 'Like'
    #     else:
    #         like.value = 'Like'
    #
    #         post.save()
    #         like.save()

        # data = {
        #     'value': like.value,
        #     'likes': post_obj.liked.all().count()
        # }

        # return JsonResponse(data, safe=False)
    # return redirect('posts')

    # print(data_)
    # question = Question.objects.get(id=data_['id'][0])
    # user = request.user.profile
    # try:
    #     userAns = UserAns.objects.get(user=user, question=question)
    #     if question.type == 'mcq':
    #         try:
    #             userAns.text = data_['ansMcq[]']
    #         except:
    #             userAns.text = None
    #     elif question.type == 'written':
    #         userAns.text = data_['ansWritten'][0]
    #         # print(data_['ansWritten'])
    #         # print(data_['ansWritten'])
    #     userAns.save()
    # except:
    #     userAns = UserAns()
    #     userAns.user = user
    #     userAns.question = question
    #     if question.type == 'mcq':
    #         try:
    #             userAns.text = data_['ansMcq[]']
    #         except:
    #             userAns.text = None
    #     elif question.type == 'written':
    #         userAns.text = data_['ansWritten'][0]
    #     userAns.save()
