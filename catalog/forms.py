from django import forms
from catalog.models import Article

class registerForm(forms.Form):
    username = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 20, required = True)
    password = forms.CharField(max_length = 20)

class articleForm(forms.Form):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {'title' : forms.TextInput}

