from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
# Create your models here.


class CustomUser(AbstractUser):
	phone_number = models.CharField(max_length=30)
	father_name = models.CharField(max_length=30, default='')
	hotel = models.ForeignKey(
        'core.Hotel',
        on_delete=models.PROTECT,
        null=True
    )


class TemporaryBanIp(models.Model):
    class Meta:
        db_table = "TemporaryBanIp"

    ip_address = models.GenericIPAddressField("IP адрес")
    attempts = models.IntegerField("Неудачных попыток", default=0)
    time_unblock = models.DateTimeField("Время разблокировки", blank=True)
    status = models.BooleanField("Статус блокировки", default=False)

    def __str__(self):
        return self.ip_address


class TemporaryBanIpAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'status', 'attempts', 'time_unblock')
    search_fields = ('ip_address',)