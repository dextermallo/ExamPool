from django import forms

class UserImageForm(forms.Form):
    image = forms.ImageField()


class registerForm(forms.Form):
    username = forms.CharField(max_length = 20, required=True)
    email = forms.EmailField(max_length = 20, required = True)
    password = forms.CharField(max_length = 20, required = True)
