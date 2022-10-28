from .models import Post, Comment
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
            'author': forms.TextInput(attrs={'id': 'author', 'value': '', 'type': 'hidden'}),
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Display Name:'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Comment Here:'}),
        }
