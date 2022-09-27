from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import *
from reacts.models import Comment


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['user', 'week','day']
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})

