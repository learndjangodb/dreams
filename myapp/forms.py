from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import DreamReal, Author, Book


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


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['title', 'name', 'birth_date']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Username'}),
            'birth_date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
        labels = {
            'name': _('Writer'),
        }
        help_texts = dict(name=_('Enter Author Name'))  # dict literal as dict constructor
        error_messages = {'name': {
            'max_length': _("This writer's name is too long")  # Dict constructor as dict literal
        }}


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class AuthorForm2(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=3,
                            widget=forms.Select(choices=TITLE_CHOICES), )
    birth_date = forms.DateField(required=False)


class BookForm2(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
