from django.contrib import admin
from . import models

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add')

    fieldsets = (
        ('Новость', {
            'fields': ('name', 'body', 'data')
        }),
        ('Изображение', {
            'fields': ('img', 'img_alt', 'img_title',)
        }),
        ('Страница', {
            'fields': ('name_url', 'page_title', 'page_description', 'page_keywords')
        }),)


class StocksAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'name_url', 'date_work', 'date_add')

    fieldsets = (
        ('Акция', {
            'fields': ('name', 'body', 'date_work')
        }),
        ('Изображение', {
            'fields': ('img', 'img_alt', 'img_title',)
        }),
        ('Страница', {
            'fields': ('name_url', 'page_title', 'page_description', 'page_keywords')
        }),)




admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Stocks, StocksAdmin)
