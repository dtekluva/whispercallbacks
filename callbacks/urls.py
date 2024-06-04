from django.urls import path

from callbacks import views


# Create your url pattern(s) here.
urlpatterns = [
    path("exchange_telecom/", views.ExchangeTelecomDlrAPIView.as_view()),
    path("route/", views.RouteDlrAPIView.as_view()),
    path("dotgo/", views.DotgoDlrAPIView.as_view()),
    path("infobip/", views.InfobipDlrAPIView.as_view()),
    path("route_two/", views.RouteDlrAPIView.as_view()),
    path("smartsms/", views.SmartsmsAPIView.as_view()),
    path("broadbased/", views.BroadbasedDlrAPIView.as_view()),
]
