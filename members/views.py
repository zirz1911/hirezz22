from django.contrib import messages
from django.shortcuts import render, redirect
from members.form import *
from members.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def workList(request):
    return render(request, 'workList.html')


# ----------------------------------------------------------------- POST PAGE ------------------------------------------------------------------


def postPage(request):  # show
    post = Item.objects.all()
    context = {'post': post}
    return render(request, 'postPage.html', context)


def selectPost(request, p_id):  # Select One
    context = {}
    context["po"] = Item.objects.get(p_id=p_id)
    return render(request, 'postSelect.html', context)


def addPost(request):  # Add Post
    if request.method == "POST":
        newForm = PostFormCreate(request.POST, request.FILES)
        if newForm.is_valid():
            newForm.save()
        messages.success(request, "Your post is successful.")
        return redirect('postPage')
    else:
        newForm = PostFormCreate()

        return render(request, 'AddPost.html', {'form': newForm})


# ----------------------------------------------------------------- POST PAGE -----------------------------------------------------------------------

# ----------------------------------------------------------------- LOGIN / LOGOUT ------------------------------------------------------------------


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You were logged in...")
            return redirect('index')
        else:
            messages.success(request, "An error to login. Please try again...")
            return redirect('login')

    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out...")
    return redirect('index')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user_id = form.cleaned_data['user_id']
            password = form.cleaned_data['password1']
            user = authenticate(user_id=user_id, password=password)
            login(request, user)
            messages.success(request, "Registration Successful...")
            return redirect('index')
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html', {'form': form, })


# ----------------------------------------------------------------- LOGIN / LOGOUT ------------------------------------------------------------------


def userProfileShow(request):
    post = myUser.objects.all()
    context = {'post': post}
    return render(request, 'userProfile.html', context)
