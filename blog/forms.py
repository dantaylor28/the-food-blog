from .models import Post
from django import forms
from cloudinary.forms import CloudinaryFileField


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'tag', 'author', 'body', 'primary_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title:'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share Your Content Here:'}),
        }

        primary_image = CloudinaryFileField()


class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'primary_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title:'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share Your Content Here:'}),
        }

        primary_image = CloudinaryFileField()