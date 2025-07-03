from django.contrib import admin
from .models import Tour, Location, Order, TourLocation

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ordered_by',
        'tour',
        'price',
        'created_at',
    )
    search_fields = ('ordered_by__email', 'tour__id')
    autocomplete_fields = ('ordered_by', 'tour')
    readonly_fields = ('price',)

class TourLocationInline(admin.TabularInline):
    model = TourLocation
    extra = 1 
    autocomplete_fields = ['location']
    ordering = ['order']

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'price', 'created_at')
    list_filter = ('category',)
    search_fields = ('id',)
    inlines = [TourLocationInline]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude')
    search_fields = ('name',)