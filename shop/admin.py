from django.contrib import admin

from .models import Item, Purchase

admin.site.register(Item)
admin.site.register(Purchase)

#
# class ItemAdmin(admin.ModelAdmin):
#     list_item = ['name', 'price']
#
#
# admin.site.register(Item, ItemAdmin)


