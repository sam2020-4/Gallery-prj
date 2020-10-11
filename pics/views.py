from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image, Category, Location


# Create your views here.
def index(request):    
    return render(request, 'index.html')

def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request, 'gallery.html', locals())

