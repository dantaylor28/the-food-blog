from .models import Post, Comment, Category
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Python code to loop through all post categories and add them to the
# empty categories array below.
# category_choices = Category.objects.all().values_list('name', 'name')
# categories = []


# for category in category_choices:
#     categories.append(category)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'extract',
            'category',
            'slug',
            'author',
            'body',
            'primary_image')

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Blog Title:'}),
            'extract': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Post Description:'}),
            # 'category': forms.Select(
            #     choices=categories, attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'format-like-this'}),
            'author': forms.TextInput(
                attrs={'id': 'author', 'value': '', 'type': 'hidden'}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '95%'}}),
        }

        primary_image = CloudinaryFileField()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['category'].widget = forms.Select(
                choices=[(cat.name, cat.name) for cat in Category.objects.all()],
                attrs={'class': 'form-control'}
        )


class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'extract', 'category', 'body', 'primary_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'extract': forms.TextInput(attrs={'class': 'form-control'}),
            # 'category': forms.Select(
            #     choices=categories, attrs={'class': 'form-control'}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '95%'}}),
        }

        primary_image = CloudinaryFileField()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['category'].widget = forms.Select(
                choices=[(cat.name, cat.name) for cat in Category.objects.all()],
                attrs={'class': 'form-control'}
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Display Name:'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Enter Comment:'}),
        }
