from django.contrib import admin
from .models import Stories, Category

# Register your models here.

class StoriesAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'size',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('code',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Stories, StoriesAdmin)
admin.site.register(Category, CategoryAdmin)