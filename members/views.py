from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
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


def selectPost(request, myUser):  # Select One
    context = {}
    context["po"] = Item.objects.get(myUser=myUser)
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


def updatePost(request, myUser):
    object = get_object_or_404(Item, myUser=myUser)
    updateForm = PostFormUpdate(request.POST or None, instance=object)

    if request.method == "POST":
        if updateForm.is_valid():
            updateForm.save()
        return redirect('postPage')
    else:
        return render(request, 'updatePost.html', {'form': updateForm, 'object': object})


def updatePostPicture(request, myUser):
    object = get_object_or_404(Item, myUser=myUser)
    updateForm = PostPicFormUpdate(request.POST or None, request.FILES, instance=object)

    if request.method == "POST":
        if updateForm.is_valid():
            updateForm.save()
        return redirect('postPage')
    else:
        return render(request, 'updatePostPic.html', {'form': updateForm, 'object': object})


def deletePost(request, myUser):
    post = get_object_or_404(Item, myUser=myUser)
    if request.method == "POST":
        post.delete()
        return redirect('postPage')
    else:
        return render(request, "deletePost.html", {'post': post})

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
