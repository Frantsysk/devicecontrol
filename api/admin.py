from django.contrib import admin
from .models import Device, DeviceInfo


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'serial', 'os')
    list_display_links = ('id', 'account')


class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'ip_address', 'country', 'cpu_load', 'memory_usage', 'disk_usage', 'timestamp')
    list_display_links = ('id', 'device')


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceInfo, DeviceInfoAdmin)
