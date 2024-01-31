from django.urls import path

from .views import detail, search

app_name = 'items'

urlpatterns = [
    path('search/', search, name='search'),
    path('item/<int:item_id>/', detail, name='detail'),


]
