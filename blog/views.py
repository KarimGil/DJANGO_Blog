from django.shortcuts import render, HttpResponse

# Create your views here.


def blogHome(request):
    return HttpResponse('all blogs here')

def blogPost(request,slug):
    return HttpResponse (f'Welcome to {slug}')