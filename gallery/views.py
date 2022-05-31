
from django.shortcuts import render
from .models import Image, Location,Category


def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, 'gallery_templates/index.html', {'images':images, 'locations':locations})







def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'gallery_templates/location.html', {'location_images': images})


def search_image(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'gallery_templates/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'gallery_templates/search_results.html', {"message": message})




