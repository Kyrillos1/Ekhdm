from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile

import uuid
# Create your models here.
from weeks.models import Week
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models.deletion import CASCADE


# from users.models import Profile

class Note(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    week = models.ForeignKey(
        Week, null=True, blank=True, on_delete=models.CASCADE)
    day = models.CharField(max_length=200, null=True)
    am = models.BooleanField(default=True, null=True, blank=True)
    pm = models.BooleanField(default=True, null=True, blank=True)
    read_bible = models.BooleanField(default=True, null=True, blank=True)
    liturgy = models.BooleanField(default=False, null=True, blank=True)
    holy_communion = models.BooleanField(default=False, null=True, blank=True)
    confession = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['-created']
