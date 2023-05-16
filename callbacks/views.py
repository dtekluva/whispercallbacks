import json
import redis
from datetime import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from callbacks.models import (
    ExchangeTelecomDlr
)


# Create your view(s) here.
class ExchangeTelecomDlrAPIView(APIView):

    def post(self, request):
        """
        DLR is sent via request headers.
        """
        raw_data = request.headers
        data = json.dumps(dict(raw_data))
        message_id = str(datetime.now())

        redis_database = redis.StrictRedis(
            host="localhost", port=6379, db=4, decode_responses=True
        )
        redis_database.set(message_id, data)

        ExchangeTelecomDlr.objects.create(
            message_id=message_id,
            message_service=raw_data.get("X-Service"),
            external_id=raw_data.get("X-External-Id"),
            recipient=raw_data.get("X-Sender"),
            message_status=raw_data.get("X-Status"),
            payload=raw_data
        )
        return Response(data={"message": "Success"}, status=status.HTTP_201_CREATED)
