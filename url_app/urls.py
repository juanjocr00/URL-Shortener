from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login
from .views import home, UrlShortener, redirect, url_list, register, download_urls, UrlFile

urlpatterns = [
    path('', home, name='home'),
    path('create/', UrlShortener, name='create'),
    path('<str:url>', redirect, name='redirect'),
    path('url_lists/', url_list, name='url_list'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_then_login, name='exit'),
    path('upload/', UrlFile, name='upload_urls'),
    path('download/', download_urls, name='download_urls'),
    
]