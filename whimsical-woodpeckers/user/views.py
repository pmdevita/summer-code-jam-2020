from django.shortcuts import render
from django.http import HttpResponse
from .models import AnonUser

def get_user(user_id):
    try:
        return AnonUser.objects.get(id=user_id)
    except AnonUser.DoesNotExist:
        return None
