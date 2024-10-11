from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

from . import forms 

# Create your views here.

#Resistering a new user
def registerUser(request):
    if request.method == 'POST':
        form = forms.Form_signup(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            #confirming the two passwords matches
            if password1 != password2:
                return redirect('/reg/signupF')
            
            try:
                #trying to save user data in the database 
                user = User.objects.create_user(username= username, email=email, password=password1)
                user.save()
                return redirect('/reg/signupS')
            except Exception as e:
                return redirect('/reg/signupF')
            
    else:
        form = forms.Form_signup()

    return render(request, 'signup.html', {'form':form})

#logs in user
#using username and password
def loginUser(request):
    if request.method == 'POST':
        form = forms.Form_Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/reg/loginS')
            else:
                return redirect('/reg/loginF')
    else:
        form = forms.Form_Login()
    return render(request, 'login.html', {'form': form})

#Minor page renderers

#signup success-failed

def signupSuccess(request):
    if request.method == "POST":
        return redirect('/reg/login')
    return render(request, 'signupSuccess.html')

def signupFailed(request):
    if request.method == "POST":
        return redirect('/reg/signup')
    return render(request, 'signupfailed.html')


#login success-failed
def loginSuccess(request):
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "dash":
            return redirect('/post/dashboard')
        elif action == "logout":
            print("Logging out")
            logout(request)
            return redirect('/reg/login')
    return render(request, 'loginSuccess.html')

def loginFailed(request):
    if request.method == "POST":
        return redirect('/reg/login')
    return render(request, 'loginFailed.html')
