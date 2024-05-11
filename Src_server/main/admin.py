from django.contrib import admin
from .models import News
from .models import Tags


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'data', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('data',)
    prepopulated_fields = {'slug': ('title',)}


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News, ThemeAdmin)
admin.site.register(Tags, TagsAdmin)
