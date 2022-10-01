from django import forms
# from froala_editor.widgets import FroalaEditor
from .models import *


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        exclude = ['user', 'slug', 'type']

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
