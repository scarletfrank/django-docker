"""django_tiger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from feed.FeedCollections import LatestEntriesFeed, HiyamiEntriesFeed, FreeStyleEntriesFeed, MemEntriesFeed

urlpatterns = [
    path('', include('plate.urls')),
    # path('demo/', include('demo.urls')),
    # path('upload/', include('upload.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('rss/blog/', LatestEntriesFeed()),
    path('rss/hiyami/', HiyamiEntriesFeed()),
    path('rss/hiyami/frst/', FreeStyleEntriesFeed()),
    path('rss/hiyami/mem_dis', MemEntriesFeed()),
    path(r'mdeditor/', include('mdeditor.urls'))
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
