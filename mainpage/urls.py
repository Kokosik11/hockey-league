from django.urls import path
from . import views
from .views import MainView, PostJsonListView, PostDetailView

urlpatterns = [
    path('', MainView.as_view(), name='mainpage'),
    path('posts-json/<int:num_posts>/', PostJsonListView.as_view(), name='posts-json-view'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]