from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):  # below showcases in what specification items will be accessed
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)
