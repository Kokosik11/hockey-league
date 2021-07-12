from django.shortcuts import render, get_object_or_404
from .models import Post

def mainpage(request):
   posts = Post.objects.filter(status=1).order_by('-created_on')

   context = {
      'posts': posts,
   }
   return render(request, 'mainpage/index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    post_object = Post.objects.get(slug=slug)

    context = {
        'post': post,
        'post_object': post_object,
    }

    return render(request, 'mainpage/post-detail.html', context)