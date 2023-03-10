from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
import json
from .models import Device, DeviceInfo


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
            # Device.objects.create(account=data['account'], serial=data['serial'], os=data['os'])
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



