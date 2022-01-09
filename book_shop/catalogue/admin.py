from django.contrib import admin

# Register your models here.
from .models import Catalogue, Category


class Cat_Admin(admin.ModelAdmin):
    list_display = ('id', 'title','category','created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','category')

class Ctg_Admin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)



admin.site.register(Catalogue, Cat_Admin)
admin.site.register(Category)