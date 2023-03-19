from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def csrf(request):
    csrf_token = get_token(request)
    return Response({'csrfToken': csrf_token})


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'status': 'success', 'token': token.key})
    else:
        return Response({'status': 'error', 'message': 'Invalid username or password.'})


@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'status': 'success'})


@api_view(['POST'])
def register_view(request):
    form = UserCreationForm(request.data)
    if form.is_valid():
        user = form.save()
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'status': 'success', 'token': token.key})
    else:
        return Response({'status': 'error', 'errors': form.errors})
