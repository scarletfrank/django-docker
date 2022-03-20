from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "所有博客信息"
    link = "/sitenews/"
    description = "Updates on changes and additions to my blogs"

    def items(self):
        return Post.objects.order_by("-created_time")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # return item.excerpt
        return item.body

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog:post_detail", args=[item.pk])


class RecentEntriesFeed(Feed):
    title = "最近的博客信息"
    link = "/sitenews/"
    description = "Updates on changes and additions to my blogs"

    def items(self):
        return Post.objects.order_by("-created_time")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # return item.excerpt
        return item.body

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog:post_detail", args=[item.pk])


class FreeStyleEntriesFeed(Feed):
    title = "有关freestyle的博客"
    link = "/sitenews/"
    description = "Updates on changes and additions to my blogs"

    def items(self):
        return Post.objects.filter(tags__name__contains="frst")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # return item.excerpt
        return item.body

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog:post_detail", args=[item.pk])


class HiyamiEntriesFeed(Feed):
    title = "有关早见的博客"
    link = "/sitenews/"
    description = "Updates on changes and additions to my blogs"

    def items(self):
        return Post.objects.filter(tags__name__contains="hiyami")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # return item.excerpt
        return item.body

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog:post_detail", args=[item.pk])


class MemEntriesFeed(Feed):
    title = "有关mem"
    link = "/sitenews/"
    description = "Updates on changes and additions to my blogs"

    def items(self):
        return Post.objects.filter(tags__name__contains="mem_dis")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # return item.excerpt
        return item.body

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog:post_detail", args=[item.pk])
