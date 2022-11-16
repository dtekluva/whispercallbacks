from django.urls import path
from call_backs.views import *


urlpatterns = [
    path('sms_callback/', dotgo_sms_callback),
    path('sms_callback_route/', route_sms_callback),   
]