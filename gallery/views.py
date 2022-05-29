from django.shortcuts import render
from .models import Image, Location
from django.http import Http404, HttpResponse


# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    print(locations)
    return render(request,'gallery_templates/index.html',locals())

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request,'gallery_templates/location.html',locals())


def search_results(request):
    
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'gallery_templates/search_results.html', locals())
    else:
        message = "You haven't searched for any image category"
        return render(request, 'gallery_templates/search_results.html', locals())



