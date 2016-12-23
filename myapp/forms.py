from django import forms
from .models import DreamReal

class LoginForm(forms.Form):
	user = forms.CharField(max_length=30)
	password  = forms.CharField(widget=forms.PasswordInput())

	def clean_message(self):
		username = self.cleaned_data.get("username")
		dbuser = DreamReal.objects.filter(name = username)

		if not dbuser:
			raise forms.ValidationError("User Does not Exist")
		return username

class ProfileForm(forms.Form):
	name = forms.CharField(max_length=100)
	picture = forms.ImageField()