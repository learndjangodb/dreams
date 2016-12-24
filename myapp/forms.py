from django import forms
from .models import DreamReal


class LoginForm(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = DreamReal.objects.filter(name=username)

        if not dbuser:
            raise forms.ValidationError("User Does not Exist")
        return username


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # some extra (optional)
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your Name"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"
