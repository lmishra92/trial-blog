from django.contrib import admin
from .models import Restaurants, RestaurantCategory
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'delivery_available', 'delivery_details']
    list_filter = ['delivery_available', 'category']
    prepopulated_fields = {'slug': ('name','postcode',)}

admin.site.register(RestaurantCategory)
admin.site.register(Restaurants)
