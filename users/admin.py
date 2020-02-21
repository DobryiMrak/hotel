from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from .models import TemporaryBanIp, TemporaryBanIpAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
	"""docstring for CustomUserAdmin"""
	add_form = CustomUserCreationForm
	fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('phone_number', 'last_name', 'first_name', 'father_name', 'hotel')}),
    )

	add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'phone_number', 'last_name', 'first_name', 'father_name', 'hotel')}
        ),
    )
	form = CustomUserChangeForm
	list_display = ['username', 'last_name', 'first_name', 'hotel', 'phone_number']
	model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TemporaryBanIp, TemporaryBanIpAdmin)
