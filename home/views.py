from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import BlogPost
# Create your views here.
def home(request):
    
    return render(request,'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        email = request.POST['email']
        contact = request.POST['contact']
        msg = request.POST['message']
        contact = Contact(name = name, contact = contact, email = email , message = msg)
        contact.save()
        messages.success(request,'Message successfully Sent!')



    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['query']

    #allPost = BlogPost.objects.all()
    allPost = BlogPost.objects.filter(title__icontains=query)
    params = {'allPost':allPost}
    return render(request,'home/search.html',params)
