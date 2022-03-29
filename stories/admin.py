from django.contrib import admin
from .models import Stories, Category, Comment

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

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)


admin.site.register(Stories, StoriesAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment, CommentAdmin)
