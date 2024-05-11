from django.shortcuts import render, redirect
from .forms import RegisterUserForm, EditDataForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered successfully')
            return redirect('register_user')
    else:
        form = RegisterUserForm()
    return render(request,'register_user.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                messages.success(request, 'User Logged in successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('user_login')
    else:
        form = AuthenticationForm()
    return render(request,'user_login.html', {'form': form})

@login_required
def profile(request):
    name = request.user
    return render(request,'profile.html', {'name': name})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'User Logged out successfully')
    return redirect('Home')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditDataForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated successfully')
            return redirect('profile')
    else:
        form = EditDataForm(instance=request.user)
    return render(request,'edit_profile.html', {'form': form})

@login_required
def change_pass_old(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'change_pass_old.html', {'form': form})

@login_required
def change_pass(request):
    if request.method == 'POST':
        form = SetPasswordForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed successfully')
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'change_pass_old.html', {'form': form})