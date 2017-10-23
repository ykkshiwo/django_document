from blog.models import BlogsPost
from django.shortcuts import render


# Create your views here.
def index(request):
    posts = BlogsPost.objects.all()
    return render(request, 'index.html', {"posts": posts})


def archive(request):
    posts = BlogsPost.objects.all()
    return render(request, "archive.html", {"posts": posts})