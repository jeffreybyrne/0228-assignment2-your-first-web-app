"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from random import randint
# import ipdb


def home_page(request):
    context = {'name': 'Jeff'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def portfolio_page(request):
    image_urls = []
    for num in range(5):
        rand_number = randint(0, 100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(rand_number))
        # ipdb.set_trace()
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    # ipdb.set_trace()
    return HttpResponse(response)


def about_me_page(request):
    my_skills = ['coding', 'being awesome', 'learning new shit']
    my_interests = ['not being bored', 'running', 'video games']
    context = {'skills': my_skills, 'interests': my_interests}
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)


urlpatterns = [
    path('home/', home_page),
    path('portfolio/', portfolio_page),
    path('about_me/', about_me_page)
]
