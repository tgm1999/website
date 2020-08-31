from django import forms
from .models import Post, CVEntry

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class CVForm(forms.ModelForm):

    class Meta:
        model = CVEntry
        fields = ('title', 'text')