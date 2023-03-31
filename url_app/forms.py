from .models import shorterURL
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewShortUrl(forms.ModelForm, LoginRequiredMixin, CreateView):
    class Meta:
        model=shorterURL
        fields = {'original_url'}
        widgets = {
            'original_url': forms.Textarea(attrs={'class': 'form-control'})
        }
        
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(error_messages={'required': None, 'invalid': None})
    username = forms.CharField(error_messages= None)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class FileUploadForm(forms.Form):
    file = forms.FileField()