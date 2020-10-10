from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import *


def main(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})