import os
import smtplib
import time
import datetime

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

class NotificationMail:

    _gmail_user="hwijung.ryu@gmail.com"
    _gmail_pwd="jafw,tie1" 
    _mail_template = "mail_template.html"
    _subject_template = "subject_template.txt"

    def send_mail(self, notification):
        # all information for notification is included in notification object
        email = notification.user_email
        contents = notification.entry
        
        constructed_html = self._build_mail_html(contents)
        constructed_subject = self._build_subject_text(contents.subject)
        
        self._send_gmail(email, constructed_subject, None, constructed_html, None)
        
        
    def _send_gmail(self, to, subject, text, html, attach):
        msg=MIMEMultipart('alternative')
        msg['From']=self._gmail_user  
        msg['To']=to
        msg['Subject']=subject
        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))

        #managing attachment 
        #part=MIMEBase('application','octet-stream')
        #part.set_payload(open(attach, 'rb').read())
        #Encoders.encode_base64(part)
        #part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
        #msg.attach(part)

        mailServer=smtplib.SMTP("smtp.gmail.com",587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self._gmail_user,self._gmail_pwd)
        mailServer.sendmail(self._gmail_user, to, msg.as_string())
        mailServer.close()

    def _send_mail_with_local_server(self, to, subject, html_text):

        # Message Container
        msg = MIMEMultipart()
        msg['Subject'] = subject

        me = "root@ryuniverse.com"
        msg['From'] = me
        msg['To'] = to
        msg.attach(MIMEText(html_text, 'html'))
          
        # Send email via local SMTP Server
        s = smtplib.SMTP('localhost')
        s.sendmail(me, to, msg.as_string())
        s.quit()

    def _build_subject_text(self, subject):
        template = open(self._subject_template, "r")
        template_subject = template.read()
        
        # replace subject with actual value
        template_subject = template_subject.replace('{{subject}}', subject)
        
        template.close()
        return template_subject
    
    def _build_mail_html(self, contents):
        template = open(self._mail_template, "r")
        template_html = template.read()
        
        # replace all keys with actual values
        for k,v in contents.iteritems():
            template_html = template_html.replace('{{%s}}' % k,v)   
        template.close()

        return template_html