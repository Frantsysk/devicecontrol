from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device, DeviceInfo
from .serializers import DeviceSerializer, DeviceInfoSerializer


@api_view(['GET'])
def api_test(request):
    content = {'status': True, 'word': 'Hello World'}
    return Response(content)


@api_view(['POST'])
def first_reg(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': True, 'id': serializer.instance.id})
    return Response({'status': False, 'errors': serializer.errors})


@api_view(['POST'])
def dev_info(request):
    device = get_object_or_404(Device, serial=request.data["serial"])
    data = request.data
    data['device'] = device.id
    serializer = DeviceInfoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": True})
    return Response({"status": False, "errors": serializer.errors})


@api_view(['GET'])
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
            'ip_address': last_info.ip_address,
            'cpu_load': last_info.cpu_load, # Add this line
            'memory_usage': last_info.memory_usage, # Add this line
            'disk_usage': last_info.disk_usage, # Add this line
        }
        device_data.append(data)
    return Response(device_data)

