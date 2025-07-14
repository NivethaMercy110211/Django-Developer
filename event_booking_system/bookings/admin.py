from django.contrib import admin
from .models import Event, Booking
from django.utils.html import format_html


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'capacity', 'seats_left', 'is_sold_out', 'event_image_preview')
    inlines = [BookingInline]

    def event_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    event_image_preview.short_description = 'Image'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'email', 'num_seats', 'booked_at')


