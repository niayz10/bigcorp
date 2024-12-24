from django.shortcuts import render
from .models import Category

def categories(request):
    categories = Category.objects.filter(parent=None)
    return  {'categories': categories}