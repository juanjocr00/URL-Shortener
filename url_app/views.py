import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import shorterURL
from django.contrib.auth.models import User
from django.http import FileResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .forms import  NewShortUrl, UserRegisterForm, FileUploadForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random, string

urls=[]

def home(request):
    return render(request, 'home.html')

@login_required
def UrlShortener(request):
    if request.method == 'POST':
        form = NewShortUrl(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url'].splitlines()
            global urls
            urls = []
            if form.cleaned_data['private'] == True:
                is_private = True
            else:
                is_private = False
            for values in original_website:
                    found = False
                    for tuple in urls:
                        if values in tuple[0]:
                            found = True
                            break
                    if found == False:
                        validator = URLValidator()
                        try:
                            validator(values)
                            valid=True
                        except ValidationError:
                            valid=False
                        if valid==True:
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
                                short_to_db= shorterURL(original_url=values, shorter_url=random_chars, username=user, private=is_private)
                                short_to_db.save()
                                urls.append((values, random_chars))
            if len(urls) == 0:
                form=NewShortUrl()
                context={'form':form}
                messages.error(request, 'No valid URL found.')
                return render(request, 'create.html', context) 
            else:                
                return render(request, 'urlcreated.html', {'shorts':urls})
        return urls
    else:
        form=NewShortUrl()
        context={'form':form}
        return render(request, 'create.html', context)   

    
   

@login_required
def UrlFile(request):           
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            original_website = file.read().decode('utf-8').splitlines()
            global urls
            urls = []
            if form.cleaned_data['private'] == True:
                is_private = True
            else:
                is_private = False
            for values in original_website:
                    found = False
                    for tuple in urls:
                        if values in tuple[0]:
                            found = True
                            break
                    if found == False:
                        validator = URLValidator()
                        try:
                            validator(values)
                            valid=True
                        except ValidationError:
                            valid=False
                        if valid==True:
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
                                short_to_db= shorterURL(original_url=values, shorter_url=random_chars, username=user, private=is_private)
                                short_to_db.save()
                                urls.append((values, random_chars))
            if len(urls) == 0:
                form = FileUploadForm()
                context={'form':form}
                messages.error(request, 'No valid URL found.')
                return render(request, 'file_upload.html', context)     
            else:                
                return render(request, 'urlcreated.html', {'shorts':urls})
        return urls 
    else:
        form = FileUploadForm()
        context={'form':form}
        return render(request, 'file_upload.html', context)  

def redirect(request, url):
    current_obj = shorterURL.objects.filter(shorter_url=url)
    try:
        current = shorterURL.objects.get(shorter_url=url)
        if current.private==True and current.username != request.user.username:
            return render(request, 'registration/login.html')
        web_visit = get_object_or_404(shorterURL, shorter_url=url)
        web_visit.visit_count +=1
        web_visit.save()
        if len(current_obj) == 0:
            return render(request, 'pagenotfound.html')
        context = {'obj': current_obj[0]}
        return render(request, 'redirect.html', context)
    except shorterURL.DoesNotExist:
        return render(request, 'login')

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



@login_required
def download_urls(request):
    global urls
    files_urls = urls
    text = '\n'.join([' -- '.join(map(str, tuple)) for tuple in files_urls])
    file_path = os.path.join(settings.MEDIA_ROOT, "Url_list.txt")
    with open(file_path, "w") as f:
        f.write("Original URl -- Short URl" + '\n')
        for item in text:
            f.write(item + "")
    response = FileResponse(open(file_path, "rb"))
    response["Content-Disposition"] = "attachment; filename=Url_list.txt"
    return response
