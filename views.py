from django.shortcuts import render
from .models import Post

# Create your views here.
def mypost(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
            #-->Try isnul=True OR title__isnull=False
    return render(request,'myblog/mypost.html',{'posts':posts})

