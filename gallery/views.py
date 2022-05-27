from turtle import title
from django.shortcuts import render

# Create your views here.
def index(request):
    title='my gallery'
    return render(request,'main/index.html',locals)
