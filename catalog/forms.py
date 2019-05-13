from django import forms
from catalog.models import Article

class registerForm(forms.Form):
    username = forms.CharField(max_length = 20, required=True)
    email = forms.EmailField(max_length = 20, required = True)
    password = forms.CharField(max_length = 20, required = True)

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {'title' : forms.TextInput}

