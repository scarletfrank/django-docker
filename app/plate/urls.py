from django.urls import path
from . import views

app_name = 'plate'

urlpatterns = [
    path('', views.index, name="index"),
    path('bizcard/', views.bizcard, name="bizcard")
]
