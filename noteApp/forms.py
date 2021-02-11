from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note

        fields = ('name', 'text')
