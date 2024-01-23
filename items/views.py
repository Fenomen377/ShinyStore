from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from items.models import Item


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    context = {'item': item}

    return render(request, 'items/detail.html', context=context)