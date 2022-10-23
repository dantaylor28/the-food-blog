from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.PostView.as_view(), name='post_view'),
    path('create_post/', views.CreateView.as_view(), name='create_post'),
]
