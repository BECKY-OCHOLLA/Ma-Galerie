from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='landing_page'),
    path('gallery/<int:gallery_id>', views.gallery,name='gallery'),
]

