from django import forms
from catalog.models import Article
from mongodbforms import DocumentForm

class registerForm(forms.Form):
    username = forms.CharField(max_length = 20)
    #email = forms.EmailField(max_length=20, required=False)
    password = forms.CharField(max_length=20)

class articleForm(DocumentForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {'title' : forms.TextInput}