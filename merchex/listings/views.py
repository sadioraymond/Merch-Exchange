# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

# Une vue est une fonction qui accepte un objet HttpRequest comme paramètre et retourne un objetHttpResponse


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
                  {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', {'listings': listings})