from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Category,Photo
# Create your views here.

def gallery(request):
    categories =Category.objects.all()
    context ={'categories': categories, 'photos': photos}
    return render(request,'photos/gallery.html',context)

def ViewPhoto(request,pk):
    photos =Photo.objects.get(id=pk)
    return render(request,'photos/photo.html', {'photos':photos})

def addPhoto(request):
    return render(request,'photos/add.html')