from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from items.models import Item, Category


# class Search(ListView):
#     template_name = 'base.html'
#
#     def get_queryset(self):
#         return Item.objects.filter(name__icontains=self.request.GET.get('q'))
#
#     def get_context_data(self, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['q'] = self.request.GET.get('q')
#         return context

def search(request):
    search_query = request.GET.get('q')
    if search_query:
        product_list = Item.objects.filter(Q(name__icontains=search_query))
    else:
        product_list = Item.objects.all()

    paginator = Paginator(product_list, 10)  # Пагинация: 10 элементов на странице

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'items/search_results.html', {'page_object': page_object, 'query': search_query})


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    context = {'item': item}

    return render(request, 'items/detail.html', context=context)

