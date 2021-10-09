from django.contrib import admin
from . import models
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add')


class StocksAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add')

admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Stocks, StocksAdmin)