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

class Contact(models.Model):
    user = models.ForeignKey(AnonUser, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.nickname


class Message(models.Model):
    contact = models.ForeignKey(Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    participants = models.ManyToManyField(Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return str(self.pk)