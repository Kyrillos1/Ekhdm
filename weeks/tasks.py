from __future__ import absolute_import, unicode_literals
from celery import shared_task
# from django.core.tasks_helper import get_generic_request, post_entity_tweet
# from .views import get_random_action
from .models import *
import time
from datetime import timedelta

@shared_task
def createWeek() -> None:
    last_week = Week.objects.first()
    if last_week:
        last_week.ended = True
        last_week.save()
    week = Week()
    week.save()
    week.created += timedelta(hours=2)
    week.save()


