import datetime
from django.shortcuts import render
from django.http import HttpResponse
from anon.models import AnonUser
from pprint import pprint

# Create your views here.


def get_user(user_id):
    try:
        return AnonUser.objects.get(id=user_id)
    except AnonUser.DoesNotExist:
        return None

def test(request):
    return  AnonUser.objects.get(id=5)
    #return HttpResponse(str(request.META))



