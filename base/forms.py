from django import forms
from .models import Website


class StoryInputForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['storybookStory']

