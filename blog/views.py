from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
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


class CommentView(generic.CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
