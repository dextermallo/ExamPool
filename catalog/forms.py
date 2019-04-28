from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length = 20)
    #email = forms.EmailField(max_length=20, required=False)
    password = forms.CharField(max_length=20)