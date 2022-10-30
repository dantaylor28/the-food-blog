from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import PostForm, EditForm, CommentForm


class HomeView(generic.ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.all()
    paginate_by = 4


class PostView(generic.DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'full_post.html',
            {
                'post': post,
                'liked': liked
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


class LikeView(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_view', args=[slug]))


# Function view to render posts within the same category to
# 'category_page.html'

def CategoryView(request, type):
    posts = Post.objects.filter(category=type)
    return render(request, 'category_page.html', {'type': type, 'posts': posts})
