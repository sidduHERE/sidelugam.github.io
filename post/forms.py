from django.contrib.auth.models import User
from django import forms

from .models import Blog , Category

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['posted_by', 'slug']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['post']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)




    class Meta:
        model = User
        fields = ['username', 'email', 'password']