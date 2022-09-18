from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import *
from comments.models import Comment

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Field, Submit

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'deadline': forms.DateInput(
                # format=('%d/%m/%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'datetime-local',  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                       })}

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if name=='deadline':
                field.widget.attrs.update({'class': 'form-control'})

            # print(name)


class SubmitForm(ModelForm):
    class Meta:
        model = Submit
        fields = '__all__'
        exclude = ['user', 'task']

        # widgets = {
        #     'deadline': forms.DateInput(
        #         # format=('%d/%m/%Y'),
        #         attrs={'class': 'form-control',
        #                # 'placeholder': 'Select a date',
        #                # 'type': 'datetime-local',  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #                })}

    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})