from django.contrib import admin
from .models import Hotel, Resedent, Nomer, Checkin


class HotelAdmin(admin.ModelAdmin):
	list_display = ['number', 'country', 'city', 'street', 'house']


admin.site.register(Hotel, HotelAdmin)
admin.site.register(Resedent)
admin.site.register(Nomer)
admin.site.register(Checkin)
