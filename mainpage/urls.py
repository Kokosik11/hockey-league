from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('posts/<slug:slug>/', views.post_detail, name='post-detail'),
]