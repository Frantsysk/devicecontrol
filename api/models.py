from django.db import models


class Device(models.Model):
    account = models.CharField(max_length=100)
    serial = models.CharField(max_length=500, unique=True)
    os = models.CharField(max_length=20)

    def __str__(self):
        return self.serial


class DeviceInfo(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    cpu_temp = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now=True)
    cpu_load = models.FloatField(null=True)
    memory_usage = models.FloatField(null=True)
    disk_usage = models.FloatField(null=True)






