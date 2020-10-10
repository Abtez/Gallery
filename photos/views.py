from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from .models import *


def main(request):
    return render(request,'index.html')