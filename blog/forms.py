from django import forms
from django.contrib.auth import get_user_model
from .models import Photo, Blog

User = get_user_model()

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Blog
        fields = ['title', 'content', 'word_count', 'contributors']

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']