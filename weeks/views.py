# from django.shortcuts import render, redirect
#
# # # Create your views here.
# #
# from django.core import paginator
#
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# #
# # from django.contrib import messages
# #
# from .models import *

# # def createWeek(request):
# #     # demomethodObj = Demomethod.objects.get(id=pk)
# #     # form = ReviewForm()
# #     week = Week()
# #     week.save()
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST)
    #     review = form.save(commit=False)
    #     review.demomethod = demomethodObj
    #     review.owner = request.user.profile
    #     review.save()
    #
    #     demomethodObj.getVoteCount
    #
    #     messages.success(request, 'Your review was successfully submitted!')
    #     return redirect('demomethod', pk=demomethodObj.id)

    # return render(request, 'notes/single-demomethod.html', {'demomethod': demomethodObj, 'form': form})