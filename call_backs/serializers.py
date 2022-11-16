from rest_framework.serializers import ModelSerializer

from call_backs.models import *


# Create your serializer(s) here.
class DotgoStatusSerializer(ModelSerializer):
    class Meta:
        model = DotgoCallback
        fields = "__all__"


class RouteStatusSerializer(ModelSerializer):
    class Meta:
        model = RouteCallback
        fields = "__all__"
