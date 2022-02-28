from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from members.form import *
from members.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


# ----------------------------------------------------------------- POST PAGE ------------------------------------------------------------------


def postPage(request):  # show
    post = Item.objects.all()
    context = {'post': post}
    return render(request, 'post/postPage.html', context)


def selectPost(request, myUser):  # Select One
    context = {}
    context["po"] = Item.objects.get(myUser=myUser)
    return render(request, 'post/postSelect.html', context)


def addPost(request):  # Add Post
    if request.method == "POST":
        if request.user.is_superuser:
            newForm = PostFormCreateAdmin(request.POST, request.FILES)
            if newForm.is_valid():
                newForm.save()
                messages.success(request, "Your post is successful.")
                return redirect('postPage')
        else:
            newForm = PostFormCreate(request.POST, request.FILES)
        if newForm.is_valid():
            # newForm.save()
            add = newForm.save(commit=False)
            add.myUser = request.user
            add.save()
            messages.success(request, "Your post is successful.")
            return redirect('postPage')
    else:
        if request.user.is_superuser:
            newForm = PostFormCreateAdmin()
        else:
            newForm = PostFormCreate()

        return render(request, 'post/AddPost.html', {'form': newForm})


def updatePost(request, myUser):
    object = get_object_or_404(Item, myUser=myUser)
    if request.user.is_superuser:
        updateForm = PostFormUpdateAdmin(request.POST or None, instance=object)
    else:
        updateForm = PostFormUpdate(request.POST or None, instance=object)

    if request.method == "POST":
        if updateForm.is_valid():
            updateForm.save()
        return redirect('postPage')
    else:
        return render(request, 'post/updatePost.html', {'form': updateForm, 'object': object})


def updatePostPicture(request, myUser):
    object = get_object_or_404(Item, myUser=myUser)
    updateForm = PostPicFormUpdate(request.POST or None, request.FILES, instance=object)

    if request.method == "POST":
        if updateForm.is_valid():
            updateForm.save()
        return redirect('postPage')
    else:
        return render(request, 'post/updatePostPic.html', {'form': updateForm, 'object': object})


def deletePost(request, myUser):
    post = get_object_or_404(Item, myUser=myUser)
    if request.method == "POST":
        post.delete()
        return redirect('postPage')
    else:
        return render(request, "post/deletePost.html", {'post': post})


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

    return render(request, 'user/login.html', {})


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
    return render(request, 'user/register_user.html', {'form': form, })


# ----------------------------------------------------------------- LOGIN / LOGOUT ------------------------------------------------------------------

# ------------------------------------------------------------ Profile / Profile Freelancer ---------------------------------------------------------


def userProfileShow(request):
    post = myUser.objects.all()
    context = {'post': post}
    return render(request, 'user/userProfile.html', context)


def freelanceProfileShow(request):
    free = Freelancer.objects.all()
    context = {'free': free}
    return render(request, 'freelanceProfile.html', context)


def addFreelancer(request):  # Add Freelance
    if request.method == "POST":
        if request.user.is_superuser:
            newForm = FreelancerCreateProfileAdmin(request.POST, request.FILES)
            chkExits = Freelancer.objects.filter(myUser=request.POST['myUser'])
            if chkExits:
                messages.success(request, "This user already have Freelancer profile.")
                return render(request, 'createFreelanceProfile.html', {'form': newForm})
            elif newForm.is_valid():
                newForm.save()
                messages.success(request, "Your post is successful.")
                return redirect('freelanceProfileShow')
        else:
            newForm = FreelancerCreateProfile(request.POST, request.FILES)
        if newForm.is_valid():
            # newForm.save()
            add = newForm.save(commit=False)
            add.myUser = request.user
            add.save()
            messages.success(request, "Create Freelancer successful.")
            return redirect('freelanceProfileShow')
    else:
        if request.user.is_superuser:
            newForm = FreelancerCreateProfileAdmin()
        else:
            newForm = FreelancerCreateProfile()

        return render(request, 'createFreelanceProfile.html', {'form': newForm})
