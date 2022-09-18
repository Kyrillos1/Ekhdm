from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile


# from users.models import Profile
class Task(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(null=True, blank=True)
    task_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/')
    deadline = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering = ['-created']


    @property
    def submitters(self):
        queryset = self.comment_set.all().values_list('user__id', flat=True)
        return queryset


class Submit(models.Model):

    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task, null=True, blank=True, on_delete=models.CASCADE)
    remark = models.CharField(max_length=200, blank=True, null=True)
    answer = models.TextField(null=True, blank=True)
    submitFile = models.FileField(
        null=True, blank=True, upload_to='profiles/', default="")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
       return f"{self.user}-{self.task}"


    class Meta:
        ordering = ['created']
        unique_together = [['user', 'task']]
    @property
    def submitURL(self):
        try:
            url = self.submitFile.url
        except:
            url = ''
        return url