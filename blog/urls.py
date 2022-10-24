from django.urls import path
# from . import views
from .views import HomeView, PostView, AddView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', PostView.as_view(), name='post_view'),
    path('create/post/', AddView.as_view(), name='create_post'),
    path('<slug:slug>/edit/', UpdatePostView.as_view(), name='edit_post'),
]
