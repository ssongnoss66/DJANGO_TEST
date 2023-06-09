from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.http import JsonResponse

# Create your views here.
@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user
    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        context = {
            'is_followed': is_followed,
            'followings_count': you.followings.count(),
            'followers_count': you.followers.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)

# def follow(request, user_pk):
#     User = get_user_model()
#     person = User.objects.get(pk=user_pk)
#     if person != request.user:
#         if person.followers.filter(pk=request.user.pk).exists():
#         # if request.user in person.followers.all():
#             person.followers.remove(request.user)
#         else:
#             person.followers.add(request.user)
#     return redirect('accounts:profile', person.username)

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('mainpg:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('mainpg:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('mainpg:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('mainpg:index')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('mainpg:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('mainpg:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mainpg:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('mainpg:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)