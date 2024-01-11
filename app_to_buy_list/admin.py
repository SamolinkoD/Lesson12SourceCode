from django.contrib import admin

from app_to_buy_list.models import Item, ItemType


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', "item_type", )
    search_fields = ('name', )
    list_filter = ('item_type', )


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
