from django.urls import path

from callbacks.views import (
    DotgoDlrAPIView,
    ExchangeTelecomDlrAPIView,
    InfobipDlrAPIView,
    RouteDlrAPIView,
    SmartsmsAPIView,

)


urlpatterns = [
    path('exchange_telecom/', ExchangeTelecomDlrAPIView.as_view()),
    path('route/', RouteDlrAPIView.as_view()),
    path('dotgo/', DotgoDlrAPIView.as_view()),
    path('infobip/', InfobipDlrAPIView.as_view()),
    path('route_two/', RouteDlrAPIView.as_view()),
    path('smartsms/', SmartsmsAPIView.as_view()),

]
