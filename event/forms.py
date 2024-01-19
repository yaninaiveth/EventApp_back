from django import forms
from .models import EventPost

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=EventPost
        fields=('name','description')