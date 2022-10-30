from django.urls import path
# from . import views
from .views import HomeView, PostView, AddView, UpdatePostView, DeleteView, CommentView, LikeView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', PostView.as_view(), name='post_view'),
    path('create/post/', AddView.as_view(), name='create_post'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='edit_post'),
    path('delete/<slug:slug>/', DeleteView.as_view(), name='delete_post'),
    path('<int:pk>/comment/', CommentView.as_view(), name='add_comment'),
    path('like/<slug:slug>', LikeView.as_view(), name='like_post'),
    path('category/<str:type>', CategoryView, name='category'),
]
