# Image upload snippets

## template
```html
<form action="/update_user_icon/" method="POST" enctype="multipart/form-data" id = "form">
    <p>
        <input id="image" type="file" class="" name="image">
    </p>
    <input type="submit" value="Submit" />
</form>
```

## show in .html
```html
<img src= "/{{ icon }}">
```

## views
```python
def update_user_icon(request):
	if (request.user.is_authenticated) & (request.method == 'POST'):		
		form = UserImageForm(request.POST, request.FILES)
		if form.is_valid():
			if Icon.objects.filter(pk=request.user) is not None:
				Icon.create_icon(request.user.id, form.cleaned_data['image'])
			else:
				Icon.objects.filter(pk=request.user.id).update(icon=form.cleaned_data['image'])
			return HttpResponseRedirect('/accounts/info/' + request.user.username)

	else:	
		form = UserImageForm()
		return render(request, 'index.html', locals())
```

## models
```python
class Icon(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    icon = models.ImageField(upload_to='media/user_icon/', max_length=None) 

    def create_icon(user, icon):
        icon = Icon(user, icon)
        icon.save()
    
    def update_icon(user, icon):
        Icon.obejcts.filter(pk=user).update(icon=icon)
```

# settings.py
```python
MEDIA_URL='media/'
MEDIA_ROOT = "media/"
```