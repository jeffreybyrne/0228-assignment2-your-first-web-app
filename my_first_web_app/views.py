from django.http import HttpResponse
from django.shortcuts import render
from random import randint


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


def favourites_page(request):
    fave_links = ['google.ca']
    context = {'fave_links': fave_links}
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)
