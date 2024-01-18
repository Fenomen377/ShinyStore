from django.urls import path
from .views import *

app_name = 'shiny'

urlpatterns = [
    path('', index, name='index'),

]
