from django import forms

from .models import Idea

class IdeaCreationForm (forms.ModelForm):
    class Meta:
        model=Idea
        fields=['long_discription', 'title', 'short_discription']
