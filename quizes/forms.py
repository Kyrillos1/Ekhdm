from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import *
from reacts.models import Comment
# from django.contrib.auth.models import Group
from users.models import Level
# from urllib import request
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field, Submit

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'date': forms.DateInput(
                # format=('%Y-%m-%d %H:%M:%S.%f'),
                format=('%Y-%m-%dT%H:%M'),
                attrs={'placeholder': 'Select a date',
                       'type': 'datetime-local',  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                       })}

    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)

        # self.fields['level'] = Level.objects.filter(group=request.user.groups.all()[0].name)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        exclude = ['user', 'quiz']
        # widgets = {
        #     'date': forms.DateInput(
        #         # format=('%d/%m/%Y'),
        #         attrs={'class': 'form-control',
        #                'placeholder': 'Select a date',
        #                'type': 'datetime-local',  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #                })}

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
# class AnswerForm(ModelForm):
#     class Meta:
#         model = Answer
#         fields = '__all__'
#         exclude = ['question']
#         # widgets = {
#         #     'date': forms.DateInput(
#         #         # format=('%d/%m/%Y'),
#         #         attrs={'class': 'form-control',
#         #                'placeholder': 'Select a date',
#         #                'type': 'datetime-local',  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
#         #                })}
#
#     def __init__(self, *args, **kwargs):
#         super(AnswerForm, self).__init__(*args, **kwargs)
#
#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})
# if name == 'date':
#     field.widget.attrs.update({'class': 'form-control'})
