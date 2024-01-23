from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from items.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()

    return render(request, 'shiny/index.html', {
        'categories': categories,
        'items': items,
    })



