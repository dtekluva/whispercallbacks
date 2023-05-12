from django.urls import path

from call_backs.views import (
    ExchangeTelecomDlrAPIView,

)


urlpatterns = [
    path('exchange_telecom/', ExchangeTelecomDlrAPIView.as_view()),

]
