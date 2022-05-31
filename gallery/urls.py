from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'


urlpatterns = [
    path('', views.index,name='index'),
    path('location/<location>', views.image_location,name='location'),
    path('search/', views.search_image, name='search_image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


