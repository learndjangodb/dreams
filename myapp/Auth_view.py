from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DreamReal, Profile
from .forms import ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def SavedProfile(request):
    saved = False

    if request.method == 'POST':
        MyProfileForm = ProfileForm(request.POST, request.FILES)

        if MyProfileForm.is_valid():
            profile = Profile()
            profile.name = MyProfileForm.cleaned_data['name']
            profile.picture = MyProfileForm.cleaned_data["picture"]
            profile.save()
            saved = True

    else:
        MyProfileForm = ProfileForm()
    return render(request, "myapp/saved.html", locals())


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page
        else:
            # Return to a 'disabled account' error message
            pass
    else:
        # Returned to "Invalid Login" error message
        pass


@login_required(login_url="/login")
def home(request):
    return render(request, "myapp/Auth/home.html")