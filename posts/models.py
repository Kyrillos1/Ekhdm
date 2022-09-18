from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile


# from users.models import Profile

class Post(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['-created']

    def num_likes(self):
        return self.liked.all().count()

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url



