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

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


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

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class DeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DeleteView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class CommentView(generic.CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CommentView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

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
# 'category_page.html'. Also retrieves all category names and adds them
# to the dropdown navbar.

def CategoryView(request, type):
    posts = Post.objects.filter(category__iexact=type.replace('-', ' '))
    context = {}
    context['type'] = type.replace('-', ' ')
    context['posts'] = posts
    category_menu = Category.objects.all()
    context['category_menu'] = category_menu
    return render(request, 'category_page.html', context)
