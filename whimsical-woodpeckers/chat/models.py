from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Texts(models.Model):
    content = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.author}-{self.date_sent}'