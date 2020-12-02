from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'plate/index.html')


def bizcard(request):
    return render(request, 'plate/bizcard.html')
