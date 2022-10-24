from django.urls import path
# from . import views
from .views import HomeView, PostView, AddView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', PostView.as_view(), name='post_view'),
    path('create/post/', AddView.as_view(), name='create_post'),
]
