from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Demomethod, Tag
from .forms import DemomethodForm, ReviewForm
from .utils import searchDemomethods, paginateDemomethods


def demomethods(request):
    demomethods, search_query = searchDemomethods(request)
    custom_range, demomethods = paginateDemomethods(request, demomethods, 6)

    context = {'demomethods': demomethods,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'demomethods/demomethods.html', context)


def demomethod(request, pk):
    demomethodObj = Demomethod.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.demomethod = demomethodObj
        review.owner = request.user.profile
        review.save()

        # demomethodObj.getVoteCount

        messages.success(request, 'Your review was successfully submitted!')
        return redirect('demomethod', pk=demomethodObj.id)

    return render(request, 'demomethods/single-demomethod.html', {'demomethod': demomethodObj, 'form': form})


@login_required(login_url="login")
def createDemomethod(request):
    profile = request.user.profile
    form = DemomethodForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()
        form = DemomethodForm(request.POST, request.FILES)
        if form.is_valid():
            demomethod = form.save(commit=False)
            demomethod.owner = profile
            demomethod.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                demomethod.tags.add(tag)
            return redirect('account')

    context = {'form': form}
    return render(request, "demomethods/demomethod_form.html", context)


@login_required(login_url="login")
def updateDemomethod(request, pk):
    profile = request.user.profile
    demomethod = profile.demomethod_set.get(id=pk)
    form = DemomethodForm(instance=demomethod)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = DemomethodForm(request.POST, request.FILES, instance=demomethod)
        if form.is_valid():
            demomethod = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                demomethod.tags.add(tag)

            return redirect('account')

    context = {'form': form, 'demomethod': demomethod}
    return render(request, "demomethods/demomethod_form.html", context)


@login_required(login_url="login")
def deleteDemomethod(request, pk):
    profile = request.user.profile
    demomethod = profile.demomethod_set.get(id=pk)
    if request.method == 'POST':
        demomethod.delete()
        return redirect('notes')
    context = {'object': demomethod}
    return render(request, 'delete_template.html', context)
