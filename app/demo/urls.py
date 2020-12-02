from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name="index"),
    # path('todo/', views.todo, name="todo"),
    # path('jsdemo/', views.jsdemo, name="jsdemo"),
    # path('table/', views.table, name="table"),
    # path('echart/', views.echart, name="echart")
]
