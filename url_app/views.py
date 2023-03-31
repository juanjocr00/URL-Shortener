import os
import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .models import shorterURL
from django.contrib.auth.models import User
from .forms import  NewShortUrl, UserRegisterForm, FileUploadForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random, string


def home(request):
    return render(request, 'home.html')

@login_required
def UrlShortener(request):
    if request.method == 'POST':
        form = NewShortUrl(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url'].split('\n')
            urls = []
            for values in original_website:
                    found = False
                    for tuple in urls:
                        if values in tuple[0]:
                            found = True
                            break
                    if found == False:
                        if shorterURL.objects.filter(original_url=values).exists():
                            created = shorterURL.objects.get(original_url=values)
                            urls.append((values, created.shorter_url))
                        else:
                            random_list = list(string.ascii_letters)
                            random_chars = ''
                            for i in range (6):
                                random_chars += random.choice(random_list)
                            while len(shorterURL.objects.filter(shorter_url=random_chars)) !=0:
                                for i in range (6):
                                    random_chars += random.choice(random_list)
                            user = request.user.username
                            short_to_db= shorterURL(original_url=values, shorter_url=random_chars, username=user)
                            short_to_db.save()
                            urls.append((values, random_chars))
            return render(request, 'urlcreated.html', {'shorts':urls})
    else:
        form=NewShortUrl()
        context={'form':form}
        return render(request, 'create.html', context)   
    return urls     

@login_required
def UrlFile(request):           
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            original_website = file.read().decode('utf-8').split('\n')
            urls = []
            for values in original_website:
                    found = False
                    for tuple in urls:
                        if values in tuple[0]:
                            found = True
                            break
                    if found == False:
                        if shorterURL.objects.filter(original_url=values).exists():
                            created = shorterURL.objects.get(original_url=values)
                            urls.append((values, created.shorter_url))
                        else:
                            random_list = list(string.ascii_letters)
                            random_chars = ''
                            for i in range (6):
                                random_chars += random.choice(random_list)
                            while len(shorterURL.objects.filter(shorter_url=random_chars)) !=0:
                                for i in range (6):
                                    random_chars += random.choice(random_list)
                            user = request.user.username
                            short_to_db= shorterURL(original_url=values, shorter_url=random_chars, username=user)
                            short_to_db.save()
                            urls.append((values, random_chars))
            return render(request, 'urlcreated.html', {'shorts':urls})
    else:
        form=NewShortUrl()
        form = FileUploadForm()
        context={'form':form}
        return render(request, 'file_upload.html', context)  
    return urls  

def redirect(request, url):
    current_obj = shorterURL.objects.filter(shorter_url=url)
    web_visit = get_object_or_404(shorterURL, shorter_url=url)
    web_visit.visit_count +=1
    web_visit.save()
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj': current_obj[0]}
    return render(request, 'redirect.html', context)

@login_required
def url_list(request):
    url_list = shorterURL.objects.all()
    paginator = Paginator(url_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'url_list.html', {'page_obj': page_obj})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user= form.cleaned_data['username']
            mail= form.cleaned_data['email']
            if User.objects.filter(username=user).exists() :
                messages.error(request, 'Username is already registered')
            else:
                if User.objects.filter(email=mail).exists():
                    messages.error(request, 'Email is already registered.')
                else:
                    form.save()
                    return render(request, 'home.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def handle_uploaded_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    with open(file_path, 'r') as file:
        content = file.read()
    os.remove(file_path)
    return content


def download_urls(request):
    data = UrlFile(request)
    loco=[]
    for i in data:
        loco.append(i)
    file_name = "archivo.txt"
    response = HttpResponse('\n'.join(loco).encode(), content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
