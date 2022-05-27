from django.shortcuts import render

# Create your views here.
def index(request):
    title='my gallery'
    return render(request,'gallery_templates/index.html',locals())

def gallery(request,gallery_id):
    return render(request,'gallery_templates/gallery.html',locals())
