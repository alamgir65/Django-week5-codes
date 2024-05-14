from django.shortcuts import render,redirect
from .forms import AddPost,CommentForm
from . import models,forms
from django.contrib.auth.decorators import login_required
#for classbased view
from django.views.generic import CreateView,UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
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

# Add post using class based view 
@method_decorator(login_required, name="dispatch")
class Add_post_ClassBasedView(CreateView):
    model = models.Post
    form_class = AddPost
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('add_posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

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

# Edit a post using class based view

@method_decorator(login_required, name="dispatch")
class Edit_post_ClassBasedView(UpdateView):
    model = models.Post
    form_class = AddPost
    template_name = 'posts/add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('Home')



@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('Home')

# Delete post using class based view 

@method_decorator(login_required, name="dispatch")
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('Home')
    pk_url_kwarg = 'id'
    

class postDetailView(DetailView):
    model = models.Post
    template_name = "posts/post_detail.html"
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        
            