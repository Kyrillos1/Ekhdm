from django.db import models
# from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
from users.models import Profile, Level


class LessonType(models.Model):
  '''
  The LessonType entries are managed by the system,
  automatically created via a Django data migration.
  '''
  POST = 1
  DEMOMETHOD = 2
  RITE = 3
  COPTICLANGUAGE = 4
  MELODY = 5
  BIBLE = 6
  THEOLOFY = 7
  DOCTRINE = 8
  HISTORY = 9
  TYPE_CHOICES = (
      (POST, 'post'),
      (DEMOMETHOD, 'وسائل الايضاح'),
      (RITE, 'الطقس'),
      (COPTICLANGUAGE, 'لغة قبطية'),
      (MELODY, 'الألحان'),
      (BIBLE, 'الكتاب المقدس'),
      (THEOLOFY, 'اللاهوت'),
      (DOCTRINE, 'عقيدة'),
      (HISTORY, 'التاريخ الكنسي'),
  )
  id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()

class Lesson(models.Model):

    type = models.ForeignKey(
        LessonType, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=1000)
    content = FroalaField(image_upload=True, null=True, blank=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(Profile, blank=True, null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(
        null=True, blank=True, upload_to='lessons/', default="profiles/user-default.png")
    public = models.BooleanField(default=False, null=True)
    level = models.ForeignKey(
        Level, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Lesson, self).save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
