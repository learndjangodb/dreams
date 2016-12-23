from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DreamReal, Profile
from .forms import ProfileForm

def SavedProfile(request):
	saved = False

	if request.method == 'POST':
		MyProfileForm = ProfileForm(request.POST, request.FILES)

		if MyProfileForm.is_valid():
			profile = Profile()
			profie.name = MyProfileForm.cleaned_data['name']
			profile.picture = MyProfileForm.cleaned_data["picture"]
			profile.save()
			saved = True

	else:
		MyProfileForm = ProfileForm()
	return render(request, "myapp/saved.html", locals())
