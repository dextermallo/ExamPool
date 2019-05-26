from django import forms
from catalog.models import Article

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {'title' : forms.TextInput}

