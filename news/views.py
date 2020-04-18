from django.shortcuts import render
from .models import Post

def my_first_simple_view(request):
    return render(
        request,
        'news/index.html',
        {
            'header': 'Index',
            'posts': Post.objects.all(),
        }
    )