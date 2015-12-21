from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class NotificationSent(models.Model):
    user = models.ForeignKey(User)
    
    data_time = models.DateTimeField(auto_now_add = True)
    
    # entry information
    author = models.CharField(max_length=32)
    subject = models.CharField(max_length=256)
    
    # notification information
    # 'email', 'sms' or something.. 
    # method = models.CharField(max_length=8)
    
    # email address like 'hwijung.ryu@gmail.com' or phone number '01012341234' 
    destination = models.CharField(max_length=32)  
    
    
def duplicate_notification_checker(user, author, subject):
    try:
        entry = NotificationSent.objects.get(user=user, author=author, subject=subject)
    except ObjectDoesNotExist:
        entry = None

    return entry

def record_sent_history(user, author, subject):
    record = NotificationSent(user=user, author=author, subject=subject)
    
    try:
        record.save()
    except ValidationError:
        return False
    
    return True
    