from django.urls import path
from api.views import api_test, first_reg, dev_info

urlpatterns = [
    path('test/', api_test),
    path('register', first_reg),
    path('info', dev_info)
]