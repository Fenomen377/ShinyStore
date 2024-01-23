from django.contrib import admin
from django.contrib.admin import ModelAdmin

from items.models import *


@admin.register(Item)
class ItemAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(ModelAdmin):
    pass
