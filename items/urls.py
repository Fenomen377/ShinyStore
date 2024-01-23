from django.urls import path

from items import views
from items.views import detail

app_name = 'items'

urlpatterns = [
    path('item/<int:item_id>/', detail, name='detail')

]
