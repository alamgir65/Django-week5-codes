from django.shortcuts import render,redirect
from .forms import RegistrationForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully')
            return redirect('Home')
    else:
        form = RegistrationForm()
    return render(request, 'authors/register.html', {'form': form, 'type' : 'Registration'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password = user_pass)
            
            if user is not None:
                messages.success(request, 'Logged in successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Information is invalid!')
                return redirect('user_login')
    else:
        form = AuthenticationForm()
    return render(request, 'authors/register.html', {'form': form, 'type' : 'Login'})


@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'authors/profile.html', {'datas' : data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            return redirect('profile')
    else:
        form = ChangeUserForm(instance=request.user)
    return render(request, 'authors/update_profile.html', {'form': form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(form)
            form.save()
            messages.success(request, 'Password changed successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'authors/pass_change.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

# def add_author(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_author')
#     else:
#         form = AuthorForm()
#     return render(request, 'authors/add_author.html' , {'form': form})
