from django.contrib import admin

from .models import Rate


# Register your models here.
class RateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'rubles', 'updated')


admin.site.register(Rate, RateAdmin)