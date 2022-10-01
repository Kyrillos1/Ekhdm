from django.db import models
from django.contrib.auth.models import User, Group
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Church(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    bio = models.TextField(blank=True, null=True)
    church_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateField()
    added = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['added']

    @property
    def imageURL(self):
        try:
            url = self.church_image.url
        except:
            url = ''
        return url





Levels = (
    (0, 'تمهيدي'),
    (1, 'الاول'),
    (2, 'الثاني'),
    (3, 'الثالث'),

)


class Level(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=15, choices=Levels, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return "%s - %s" % (self.group.name, self.name)

    class Meta:
        ordering = ['created']


TYPES_EDUCATION = (
    ('المرحلة الإبتدائية', 'المرحلة الإبتدائية'),
    ('المرحلة الإعدادية', 'المرحلة الإعدادية'),
    ('الثانوية العامة', 'الثانوية العامة'),
    ('الثانوي الفنية صنايع', 'الثانوي الفنية صنايع'),
    ('الثانوي الفنية تجاري', 'الثانوي الفنية تجاري'),
    ('الثانوي الفنية زراعي', 'الثانوي الفنية زراعي'),
    ('سباحة وفنادق', 'سباحة وفنادق'),
    ('الدبلوم', 'الدبلوم'),
    ('البكالوريوس', 'البكالوريوس'),
    ('الدبلوم العالي', 'الدبلوم العالي'),
    ('الماجستير', 'الماجستير'),
    ('الدكتوراه', 'الدكتوراه'),
)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # church = models.ForeignKey(
    #     Church, on_delete=models.CASCADE, null=True, blank=True)
    levels = models.ManyToManyField(
        Level, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)

    # skill = models.CharField(max_length=15, null=True, blank=True)

    bio = models.TextField(blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    job = models.CharField(max_length=200, blank=True, null=True)
    Educational_qualification = models.CharField(choices=TYPES_EDUCATION, max_length=200, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

    @property
    def allNotes(self):
        queryset = self.note_set.all()
        return queryset

    def get_levels(self):
        return self.levels.all()


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']

    def __str__(self):
        return str(self.pk)
