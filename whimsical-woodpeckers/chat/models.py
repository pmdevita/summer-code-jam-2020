from django.db import models
from user.models import AnonUser

'''class Conversation(models.Model):
    id = models.AutoField
    participants = []

class Messages(models.Model):
    id = models.AutoField
    sender = user.id
    reciever = user.id
    content = models.CharField(max_length=280)
    type = models.IntegerField()
    time_date = models.DateField()
    pk = (sender+"_"+reciever+"_"+time_date)'''
