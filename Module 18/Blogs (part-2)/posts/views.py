from django.shortcuts import render,redirect
from .forms import AddPost
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('add_posts')
    else:
        form = AddPost()
    return render(request, 'posts/add_post.html', {'form':form})

@login_required
def edit_post(request , id):
    post = models.Post.objects.get(pk=id)
    form = AddPost(instance=post)
    if request.method == 'POST':
        form = AddPost(request.POST , instance=post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('Home')
    return render(request, 'posts/add_post.html', {'form':form})

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('Home')
