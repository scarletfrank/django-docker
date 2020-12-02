from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post


# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

# def index(request):
#     return render(request, 'blog/myindex.html', context={
#         'title': '我的博客首页',
#         'welcome': '欢迎访问我的博客首页'
#     })

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_time')
    template_name = 'blog/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
