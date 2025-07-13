from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display=['Name','Desc']
    search_fields=['Name']
    
@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display=['name','category','price','quantity','featured']
    search_fields=['name','desc']
    list_filter=['category','featured']
    list_editable=['quantity','featured']



