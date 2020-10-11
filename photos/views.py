from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import *


def main(request):
    images = Image.objects.all()
    category = Category.objects.all()
    context = {'images':images, 'category':category}
    return render(request,'index.html',context)

def search_images(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_category})

    else:
        return render(request, 'search.html')
    