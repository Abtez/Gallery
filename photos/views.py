from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import *


def main(request):
    images = Image.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{'images':images, 'category':category})

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
    
def copy(request):
    return render(request,'copy.html')
    