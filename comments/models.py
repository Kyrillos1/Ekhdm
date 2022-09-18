from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile
from tasks.models import Task
from books.models import Book
from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, null=True,  blank=True, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return str(self.body)

    class Meta:
        ordering = ['created']

class Save(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, null=True,  blank=True, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task, null=True, blank=True, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return str(self.user.name)

    class Meta:
        ordering = ['-created']


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, null=True, blank=True, on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task, null=True, blank=True, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    class Meta:
        ordering = ['-created']
