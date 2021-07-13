from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import View, TemplateView, DetailView
from django.http import JsonResponse

# def mainpage(request):
#    posts = Post.objects.filter(status=1).order_by('-created_on')

#    context = {
#       'posts': posts,
#    }
#    return render(request, 'mainpage/index.html', context)

class MainView(TemplateView):
   template_name = 'mainpage/index.html'

class PostDetailView(DetailView):
   template_name = 'mainpage/post-detail.html'
   model = Post

class PostJsonListView(View):
   def get(self, *args, **kwargs):
      print(kwargs)
      upper = kwargs.get('num_posts') # three posts
      lower = upper - 3 # zero posts
      posts = list(Post.objects.values()[lower:upper])
      posts_size = len(Post.objects.all())
      max_size = True if upper >= posts_size else False
      return JsonResponse({'data': posts, 'max': max_size}, safe=False)

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug, status=1)
#     post_object = Post.objects.get(slug=slug)

#     context = {
#         'post': post,
#         'post_object': post_object,
#     }

#     return render(request, 'mainpage/post-detail.html', context)