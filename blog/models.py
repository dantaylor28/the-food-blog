from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    tag = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    primary_image = CloudinaryField('image', default='placeholder')

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return f"{self.title} | {self.author}"

    def num_of_likes(self):
        return self.likes.count()

    
