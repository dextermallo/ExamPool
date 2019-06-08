from django import forms
from catalog.models import Article, Comment

class registerForm(forms.Form):
    username = forms.CharField(max_length = 20, required=True)
    email = forms.EmailField(max_length = 20, required = True)
    password = forms.CharField(max_length = 20, required = True)

class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {'title' : forms.TextInput}

class voteForm(forms.Form):
    is_article = forms.CharField()
    comment_id = forms.CharField()
    goodbad = forms.CharField(max_length = 20, required=True)

class favoriteForm(forms.Form):
    article_id = forms.CharField()

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class tagForm(forms.Form):
    tag_name = forms.CharField()

class pageForm(forms.Form):
    page = forms.CharField()

class searchForm(forms.Form):
    check = forms.CharField()
    tag = forms.CharField(required=False)
    title = forms.CharField(required=False)
    content = forms.CharField(required=False)
    author = forms.CharField(required=False)
    sort = forms.CharField(required=False)