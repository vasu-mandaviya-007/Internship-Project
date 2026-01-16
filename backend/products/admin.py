from django.contrib import admin
from .models import Products, Variants, Images
from categories.models import Categories
import nested_admin

#admin.site.register(Products)
admin.site.register(Categories)
#admin.site.register(Variants)
#admin.site.register(Images)

class ImagesvariantInline(nested_admin.NestedTabularInline):
    model = Images
    extra = 1

@admin.register(Variants)
class VariantsAdmin(nested_admin.NestedModelAdmin):
    inlines = [ImagesvariantInline]
    


class ProductvariantInline(nested_admin.NestedTabularInline):
    model = Variants
    extra = 1
    inlines = [ImagesvariantInline]

@admin.register(Products)
class ProductsAdmin(nested_admin.NestedModelAdmin):
    inlines = [ProductvariantInline]
    list_display = ('title', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published',)


# Register your models here.
