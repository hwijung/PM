from django.db import models
from django.contrib.auth.models import User

class NotificationSent(models.Model):
    user = models.ForeignKey(User)
    
    data_time = models.DateTimeField(auto_now_add = True)
    
    # entry information
    author = models.CharField(max_length=32)
    subject = models.CharField(max_length=256)
    
    # notification information
    method = models.CharField(max_length=8)
    