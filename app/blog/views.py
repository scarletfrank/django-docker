import markdown

from django.shortcuts import render, get_object_or_404
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

# 重写方法[参考](https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/)
# 参考[源码](https://github.com/django/django/blob/145f6c3ed6e8856078e2d04ff2567e9fb4a17930/django/views/generic/detail.py#L102)


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        post.body = markdown.markdown(post.body, extensions=[
                                      'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc', ])
        context['post'] = post
        return context
