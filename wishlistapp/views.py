from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  SignupForm, SigninForm ,WishForm
from django.contrib.auth import login, authenticate, logout
from .models import Wish


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("user-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('user-list')
    context = {
        "form":form,
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("signin")

def home(request):
    return render(request, 'home.html')


def list(request,):
    wishs = Wish.objects.all().order_by("-date")
    context = {
        "wishs": wishs,
    }
    return render(request, 'list.html',context)




def wish_create(request):
    form = WishForm()
    if request.user.is_anonymous:
        return redirect('signin')
    if request.method == "POST":
        form = WishForm(request.POST, request.FILES)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.owner = request.user
            wish.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'wish_create.html', context)

#def create_list(request):
#    form = ListForm()
#    if request.user.is_anonymous:
#        return redirect('signin')
#    if request.method == "POST":
#        form = ListForm(request.POST)
#        if form.is_valid():
#            list = form.save(commit=False)
#            list.owner = request.user
#            list.save()
#            return redirect('user-list')
#    context = {
#        "form":form,
#    }
#    return render(request, 'create_list.html', context)


def user_list(request,):
    context = {
        "msg":"hhhhh"
    }
    return render(request, 'user_list.html',context)

#def wish_delete(request, wish_id):
#    wish_obj = Restaurant.objects.get(id=wish_id)
#    wish_obj.delete()
#    return redirect('wish-list')

def discover(request,):
    wishs = Wish.objects.all().order_by("-date")
    context = {
        "wishs": wishs,
    }
    return render(request, 'discover.html',context)
