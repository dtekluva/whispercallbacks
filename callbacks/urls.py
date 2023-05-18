from django.urls import path

from callbacks.views import (
    ExchangeTelecomDlrAPIView,
    RouteDlrAPIView,

)


urlpatterns = [
    path('exchange_telecom/', ExchangeTelecomDlrAPIView.as_view()),
    path('route/', RouteDlrAPIView.as_view()),

]
