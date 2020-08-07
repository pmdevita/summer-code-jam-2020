  
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import AnonUser
import datetime


class AnonBackend(ModelBackend):    
    def authenticate(self, request, username=None, password=None):
        id = request.session.get("ID")
        if not id:
            user = AnonUser.objects.create(last_seen=datetime.datetime.now())
            request.session['ID'] = user.id
        else:
            user = AnonUser.objects.get(id=id)

        return user