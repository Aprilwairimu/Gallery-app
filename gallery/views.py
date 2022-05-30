from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Category,Photo
# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    # if category == None:
    #     else:
    #         photos =Photo.objects.filter(category__name=category)

    categories =Category.objects.all()
    photos =Photo.objects.all()
    context ={'categories': categories, 'photos': photos}
    return render(request,'photos/gallery.html',{'categories': categories, 'photos': photos})

def ViewPhoto(request,pk):
    photos =Photo.objects.get(id=pk)
    return render(request,'photos/photo.html', {'photos':photos})

def addPhoto(request):
    categories =Category.objects.all()

    # if request.method = 'POST':
    #     data = request.POST
    #     image = request.FILES.get('image')

    context ={'categories': categories}
    return render(request,'photos/add.html')

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})

def home(request):
    return render(request, 'home.html')