from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('sms/', views.SmsLogListView.as_view(), name='sms'),
    path('templates/', views.SmsTemplatesView.as_view(), name='templates'),
    path('settings/', views.SmsSettingsView.as_view(), name='settings'),
    path('send/', views.SmsSendView.as_view(), name='send'),
]
