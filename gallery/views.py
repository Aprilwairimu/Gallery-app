from django.shortcuts import render
from django.http  import HttpResponse,Http404
# Create your views here.

def gallery(request):
    return render(request,'photos/gallery.html')

def ViewPhoto(request):
    return render(request,'photos/photo.html')

def addPhoto(request):
    return render(request,'photos/add.html')