from django.urls import path
from api.views import api_test

urlpatterns = [
    path('test/', api_test)
]