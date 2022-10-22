from django.shortcuts import render
from django.views import generic
from .models import Post


class HomeView(generic.ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.all()
    paginate_by = 3
