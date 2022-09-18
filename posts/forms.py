from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Post
from comments.models import Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','liked']
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input'})

        # self.fields['description'].widget.attrs.update(
        #     {'class': 'input'})

