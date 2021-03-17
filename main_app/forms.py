from django import forms
from .models import Post, Profile, City

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'body']

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['first_name', 'last_name', 'current_city']

class CityForm(forms.ModelForm):
  class Meta:
    model = City
    fields = ['name', 'photo_url']

