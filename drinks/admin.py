from django.contrib import admin

from drinks.models import Drink


class DrinkAdmin(admin.ModelAdmin):
    list_display = ("name", "has_alcohol")


# Register your models here.
admin.site.register(Drink, DrinkAdmin)
