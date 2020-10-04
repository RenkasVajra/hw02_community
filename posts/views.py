from .models import Group, Post

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.ordering['12']
    return render(request, "group.html",{
        "group": group, 
        "posts": posts,
    })  

def index(request):
    latest = group.posts.ordering[:11]
    return render(request, "index.html", {
        "posts": latest,
    }) 
    
# Post.objects.filter(group=group).order_by("-pub_date")[:12]  
# Post.objects.order_by("-pub_date")[:11]