from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from comments.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        labels = {
            'body': 'Add your comment'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

