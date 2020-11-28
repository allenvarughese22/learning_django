from django.shortcuts import render

from django.http import  HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse('this is inside about')

def contact(request):
    return HttpResponse('this is inside contact')

def tracker(request):
    return HttpResponse('this is inside tracker')


def search(request):
    return HttpResponse('this is inside search')


def product(request):
    return HttpResponse('this is inside productview')



def checkout(request):
    return HttpResponse('this is inside checkout')