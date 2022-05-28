from django.shortcuts import render
from .models import image, location
from django.http import Http404, HttpResponse


# Create your views here.
def index(request):
    images = image.objects.all()
    locations = location.objects.all()
    print(locations)
    return render(request,'gallery_templates/index.html',locals())

def image_location(request, location):
    images = image.filter_by_location(location)
    print(images)
    return render(request,'gallery_templates/location.html',locals())
