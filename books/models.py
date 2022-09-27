from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile,Level


# from users.models import Profile
class Book(models.Model):

    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    writer = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(null=True, blank=True)
    bookFile = models.FileField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    valid = models.BooleanField(default=False, null=True)
    public = models.BooleanField(default=False, null=True)
    level = models.ForeignKey(
        Level, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']

    @property
    def bookURL(self):
        try:
            url = self.bookFile.url
        except:
            url = ''
        return url


#
# class Like(models.Model):
#     user = models.ForeignKey(
#         Profile, null=True, blank=True, on_delete=models.CASCADE)
#     book = models.ForeignKey(
#         Book, null=True, blank=True, on_delete=models.CASCADE)
#     positive = models.BooleanField(default=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False)
