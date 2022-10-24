from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(generic.ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.all()
    paginate_by = 4


class PostView(generic.DetailView):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'full_post.html',
            {
                'post': post
            },
        )


class AddView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm


class DeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
