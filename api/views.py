from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
import json
from .models import Device, DeviceInfo
from django.db.models import Subquery, OuterRef
from django.core import serializers


def api_test(request):
    content = {'status': True, 'word': 'Hello World'}
    return JsonResponse(content)


@csrf_exempt
def first_reg(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dev = Device(account=data['account'], serial=data['serial'], os=data['os'])
            dev.save()
        except Exception as er:
            return JsonResponse({'status': False, 'error': er.args[0]})
        else:
            content = {'status': True, 'id': dev.id}
            return JsonResponse(content)


@csrf_exempt
def dev_info(request):
    data = json.loads(request.body)
    device = get_object_or_404(Device, serial=data["serial"])
    DeviceInfo.objects.create(
                              device=device,
                              cpu_temp=data.get('cpu_temp'),
                              cpu_load=data.get('cpu_load'),
                              memory_usage=data.get('memory_usage'),
                              disk_usage=data.get('disk_usage'),
                              ip_address=data.get('ip_address'),
                              country=data.get('country'),
                              )
    return JsonResponse({"status": True})


@csrf_exempt
def show_status(request):
    devices = Device.objects.all()
    device_data = []
    for device in devices:
        last_info = device.deviceinfo_set.latest('timestamp')
        data = {
            'device__account': last_info.device.account,
            'device__serial': last_info.device.serial,
            'device__os': last_info.device.os,
            'cpu_temp': last_info.cpu_temp,
            'ip_address': last_info.ip_address
        }
        device_data.append(data)
    return JsonResponse(device_data, safe=False)





