from django.urls import path

from callbacks.views import (
    ExchangeTelecomDlrAPIView,

)


urlpatterns = [
    path('exchange_telecom/', ExchangeTelecomDlrAPIView.as_view()),

]
