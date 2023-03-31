from .models import shorterURL
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewShortUrl(forms.ModelForm):
    class Meta:
        model=shorterURL
        fields = {'original_url', 'private'}
        widgets = {
            'original_url': forms.Textarea(attrs={'class': 'form-control'}),
            'private': forms.CheckboxInput(attrs={'class': 'mi-clase-css'})
        }
        


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(error_messages={'required': None, 'invalid': None})
    username = forms.CharField(error_messages= None)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class FileUploadForm(forms.Form, forms.ModelForm):
    file = forms.FileField()
    class Meta:
        model=shorterURL
        fields = {'private'}
        widgets = {
                'private': forms.CheckboxInput(attrs={'class': 'mi-clase-css'})
            }