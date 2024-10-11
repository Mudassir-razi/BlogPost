from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import logout
from . import forms
from . import models

# Create your views here.
#rendering all the posts

def viewDashboard(request):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "post":
            return redirect('/post/newpost')
        elif action == "logout":
            logout(request)
            return redirect('/reg/login')
    posts = models.post.objects.all()

    return render(request, "dashboard.html", {"posts" : posts})

def createPost(request):
    if request.method == "POST":
        form = forms.Form_createPost(request.POST)
        action = request.POST.get("action")
        if action == "post" and form.is_valid():
            print("Post done")
            blogpost = form.save(commit=False)
            blogpost.writer = request.user
            blogpost.date = timezone.now()
            blogpost.save()
            print("Post done")
            return redirect('/post/dashboard')
        elif action == "cancel":
            return redirect('/post/dashboard')
        print(form.errors)
    else: 
        form = forms.Form_createPost()
    return render(request, 'post.html', {"form": form})
        