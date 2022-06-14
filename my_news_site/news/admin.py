from django.contrib import admin

# Register your models here.
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'creation_date', 'date_of_change', 'is_published')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
