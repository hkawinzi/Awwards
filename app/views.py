from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *

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
    return render(request, 'main/index.html', {'posts': post, 'form': form})

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

