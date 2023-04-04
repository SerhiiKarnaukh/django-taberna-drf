from django.contrib import admin
import admin_thumbnails

from .models import Category, Product, ProductGallery


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class CategoryAdminModel(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    list_display_links = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name", )}


class ProductAdminModel(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'date_added',
        'image',
    )
    list_display_links = ('name', )
    search_fields = (
        'name',
        'description',
    )
    list_editable = ('price', )
    list_filter = (
        'date_added',
        'category',
    )
    prepopulated_fields = {"slug": ("name", )}
    inlines = [ProductGalleryInline]


admin.site.register(Category, CategoryAdminModel)
admin.site.register(Product, ProductAdminModel)
admin.site.register(ProductGallery)
