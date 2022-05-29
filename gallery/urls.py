from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('location/<location>', views.image_location,name='location'),
    path('search/', views.search_results, name='search_results')
]

