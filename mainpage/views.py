from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import View, TemplateView, DetailView
from django.http import JsonResponse
from match.models import Match


class MainView(TemplateView):
   template_name = 'mainpage/index.html'

   def get_context_data(self, **kwargs):
      context = super(MainView, self).get_context_data(**kwargs)
      context['last_match'] = Match.objects.latest('date')
      return context

# Sales.objects.all().extra(select={'month': 'MONTHNAME(date)'}).values('month').annotate(total=SUM('amount')).values('month', 'total')

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
