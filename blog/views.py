from django.shortcuts import render, HttpResponse
from .models import BlogPost

# Create your views here.


def blogHome(request):
    allPost = BlogPost.objects.all()
    context = {'allPost': allPost}
    return render(request,"blog/blogHome.html",context)

def blogPost(request,slug):
    post = BlogPost.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,"blog/blogPost.html",context)
