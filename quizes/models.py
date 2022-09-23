from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models.deletion import CASCADE


# from users.models import Profile
QUIZTYPE = (
    ('final', 'final'),
    ('Not final', 'Not final'),
)

class Quiz(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)

    type = models.CharField(max_length=10, choices=QUIZTYPE, null=True, blank=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    date = models.DateTimeField(null=True, blank=True, editable=True)
    time = models.IntegerField(help_text="duration of the quiz in minutes", null=True, blank=True)
    desc = models.TextField(blank=True, null=True)
    number_of_questions = models.IntegerField(null=True, blank=True)
    valid = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        # return f"{self.title}-{self.topic}"
        return self.title

    class Meta:
        ordering = ['-valid', '-date']

    @property
    def get_questions(self):
        return self.question_quiz.all()

    @property
    def questions(self):
        queryset = self.question_quiz.all().values_list('text','grade','question_image','type','wrongAnswers','correctAnswers')
        return queryset
    # def admitors(self):
    #     queryset = self.question_quiz.all().values_list('text', 'grade', 'question_image', 'type', 'wrongAnswers',
    #                                                     'correctAnswers')
    #     return self._quiz.all()
    # def num_likes(self):
    #     return self.liked.all().grade.all().sum()


TYPE = (
    ('mcq', 'mcq'),
    ('written', 'written'),
)


class Question(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, null=True, blank=True, on_delete=models.CASCADE, related_name="question_quiz")
    text = models.TextField(blank=True, null=True)
    grade = models.IntegerField(null=True, blank=True)
    question_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    type = models.CharField(max_length=10, choices=TYPE, null=True, blank=True)
    wrongAnswers = models.CharField(max_length=200, null=True, blank=True)
    correctAnswers = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    @property
    def QuestionURL(self):
        try:
            url = self.question_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.text)

    class Meta:
        ordering = ['created']

    def get_answers(self):
        return self.answer_set.all()



class UserAns(models.Model):
    user = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    grade = models.IntegerField(null=True, blank=True,default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.text)

    class Meta:
        ordering = ['created']
        unique_together = [["user", "question"]]


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
