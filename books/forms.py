from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Book
from comments.models import Comment

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['user', 'valid']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
