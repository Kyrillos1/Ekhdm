from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.deletion import CASCADE
# from users.models import Profile

class Week(models.Model):
    ended = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return str(self.created)

    class Meta:
        ordering = ['-created']