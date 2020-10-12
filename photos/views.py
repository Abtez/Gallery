from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import *


def main(request):
    images = Image.objects.all()
    category = Category.objects.all()
    location = Location.objects.all()
    return render(request,'index.html',{'images':images, 'category':category, 'location':location})

def search_images(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_category)

        return render(request, 'search.html',{"message":message,"image": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})
    
def view_by_location(request,location):
    image_location = Image.filter_by_location(location)
    print(image_location)
    return render(request, 'location.html',{"location": image_location})
    