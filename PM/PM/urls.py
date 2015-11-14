"""PM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os.path

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from alarms import views

static = os.path.join ( os.path.dirname( __file__ ), 'static' )

urlpatterns = [ 
	# Administration 
    url(r'^admin/', include(admin.site.urls)),
 
    # Alarm Management 
    url(r'^$', views.home, name='alarms.views.home'),
    url(r'^alarms/$', views.alarms_view, name='alarms.views.alarms_view'),
    url(r'^alarms/create/$', views.alarm_create_view, name='alarms.views.alarm_create_view'),
    url(r'^alarms/activate/$', views.alarm_activate, name='alarms.views.alarm_activate'),    
    url(r'^alarms/([\w ]+)/$', views.alarm_view, name='alarms.views.alarms_view'),

   
    # Session Management
    url(r'^login/$', views.login_view, name='alarms.views.login'),
    url(r'^logout/$', views.logout_view, name='alarms.views.logout'),
    url(r'^signup/$', views.signup_view, name='alarms.views.signup'),
    url(r'^signup/success/$', TemplateView.as_view(
            template_name='signup_success.html'), name='alarms.views.signup_success' ), 
     
    # Settings 
    url(r'^settings/$', views.settings_view, name='alarms.views.settings'),

    # Media/Static
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': static }),

]
