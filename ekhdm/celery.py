# from celery.schedules import crontab
# from celery.task import periodic_task
#
#
# # @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
# @periodic_task(run_every=crontab(minute=1))
# def every_monday_morning():
#     print("This is run every Monday morning at 7:30")

# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ekhdm.settings')
# app = Celery('ekhdm')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
#


from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ekhdm.settings")

app = Celery("ekhdm")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "Create_Week": {
        "task": "weeks.tasks.createWeek",
        # "schedule": crontab(minute=0, hour=8),
        # "schedule": crontab(minute=0, hour=0, day_of_week='friday')
        "schedule": crontab(minute=2),
    },
    # "post-quote-tweet-every-day-at-18h": {
    #     "task": "quotes.tasks.post_quote_tweet",
    #     "schedule": crontab(minute=0, hour=18),
    # },
}
# app.conf.redis_url="redis://localhost:6380"


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")