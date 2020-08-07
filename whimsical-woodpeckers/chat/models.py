from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from anon.models import AnonUser
from django.urls import reverse

class Text(models.Model):
    id = models.AutoField()
    sender = models.ForeignKey(AnonUser, on_delete=models.CASCADE)
    reciever = models
    content = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'{self.author}-{self.date_sent}'

    def get_absolute_url(self):
        return reverse('chat')