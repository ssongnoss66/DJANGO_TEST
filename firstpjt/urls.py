"""firstpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# WARNINGS: (urls.W005) URL namespace 'MayTwentyThird' isn't unique. You may not be able to reverse all URLs in this namespace
# https://comdoc.tistory.com/entry/URL-namespace-xxx-isnt-unique
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mainpg.urls')),
    path('admin/', admin.site.urls),
    path('apps/', include('apps.urls')),
    path('MarchTwentyThird/', include('MarchTwentyThird.urls')),
    path('articles/', include('articles.urls')),
    path('todos/', include('todos.urls')),
    path('accountbooks/', include('accountbooks.urls')),
    path('accounts/', include('accounts.urls')),
    path('albums/', include('albums.urls')),
    path('reviews/', include('reviews.urls')),
    path('hospitals/', include('hospitals.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)