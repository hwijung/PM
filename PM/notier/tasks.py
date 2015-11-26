from __future__ import absolute_import

from django.contrib.auth.models import User
from notier.mail.mail import NotificationMail
from notier.models import duplicate_notification_checker
def send_notification(user, matched):
    
    for entry in matched:
        # check whether the notification has been sent (use author, title for checking)
        if duplicate_notification_checker(user, entry['author'], entry['subject']) == None:
            
        # if it hasn't been sent, send notification 
    
            # write it on DB
    
    
    pass
