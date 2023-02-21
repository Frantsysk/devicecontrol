from django.http import HttpResponse, JsonResponse


def api_test(request):
    content = {'ok': True, 'word': 'Hello World'}
    return JsonResponse(content)

