from .models import Post, Comment
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'extract', 'category', 'slug', 'author', 'body', 'primary_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title:'}),
            'extract': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief Description Of Post:'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'id': 'author', 'value': '', 'type': 'hidden'}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '95%'}}),
        }

        primary_image = CloudinaryFileField()


class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'extract', 'body', 'primary_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'extract': forms.TextInput(attrs={'class': 'form-control'}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '95%'}}),
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
