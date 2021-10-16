from django.contrib import admin
from . import models


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add')


class StocksAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'name_url', 'date_work')


admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Stocks, StocksAdmin)
