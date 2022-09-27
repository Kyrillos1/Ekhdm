from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm
from reacts.forms import CommentForm
from reacts.models import Like
from .utils import searchPosts, paginatePosts


def posts(request):
    posts, search_query = searchPosts(request)
    custom_range, posts = paginatePosts(request, posts, 6)
    form = CommentForm()
    context = {'posts': posts,
               'search_query': search_query,
               'custom_range': custom_range,
               'form': form
               }
    return render(request, 'posts/posts.html', context)


def post(request, pk):
    postObj = Post.objects.get(id=pk)
    form = CommentForm()

    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     comment = form.save(commit=False)
    #     comment.post = postObj
    #     comment.user = request.user.profile
    #     comment.save()

        # postObj.getVoteCount

        # messages.success(request, 'Your comment was successfully submitted!')
        # return redirect('post', pk=postObj.id)

    return render(request, 'posts/single-post.html', {'post': postObj, 'form': form})



@login_required(login_url="login")
def createPost(request):
    profile = request.user.profile
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = profile
            post.save()

            return redirect('posts')

    context = {'form': form}
    return render(request, "posts/post_form.html", context)


@login_required(login_url="login")
def updatePost(request, pk):
    profile = request.user.profile
    post = profile.post_set.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        # newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('posts')

    context = {'form': form, 'post': post}
    return render(request, "posts/post_form.html", context)
# 
# 
@login_required(login_url="login")
def deletePost(request, pk):
    profile = request.user.profile
    post = profile.post_set.get(id=pk)
    if post:
        if request.method == 'POST':
            post.delete()
            return redirect('posts')


    context = {'object': post}
    return render(request, 'delete_template.html', context)
