from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *
from .models import Project


# Create your views here.
def index(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, '/index.html', {'posts': post, 'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            form = SignupForm()
            register_form = {
                'form': form,
            }
        return redirect(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'profile/profile.html')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST)
        profile_form = UpdateUserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm()
        profile_form = UpdateUserProfileForm()
    return render(request, 'main/edit.html')


def profile_view(request):
    profile = Profile.get_profile_data()
    profile_data = {
        'profile': profile
    }

    return render('profile/profile.html', profile_data)


def upload(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, '/upload.html', {'post': post, 'form': form})


def home(request):

    current_user = request.user
    project_images = Project.fetch_all_images()
    image_params = {
        'all_images': project_images,
        'current_user': current_user,
    }
    return render(request, 'index.html', image_params)


def rate(request):
    ratings = Rate.objects.all()
    rate_params = {
        'ratings': ratings
    }

    return render('view_project.html', rate_params)





