import json
import traceback
from datetime import datetime

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from callbacks.models import ExchangeTelecomDlr
from callbacks.serializers import MessageStatusSerializer
from helpers.redis_db import (
    connect_dotgo_database,
    connect_exchange_database,
    connect_infobip_database,
    connect_route_database
)


# Create your view(s) here.
class ExchangeTelecomDlrAPIView(APIView):
    message_service_choices = {
        "wprohtmt": "PROMOTIONAL",
        "wtrxhtmo": "TRANSACTIONAL",
        "wprohtmo": "PROMOTIONAL"
    }
    message_status_choices = {
        "200": "DELIVERED",
        "400": "EXPIRED",
        "403": "DELETED",
        "404": "UNDELIVERED",
        "405": "UNKNOWN",
        "406": "ACCEPTED",
        "407": "REJECTED"
    }

    def post(self, request):
        """
        DLR is sent via request headers.
        """
        raw_data = request.headers
        data = json.dumps(dict(raw_data))
        message_id = str(datetime.now())

        connect_exchange_database.set(message_id, data)

        ExchangeTelecomDlr.objects.create(
            message_id=message_id,
            message_service=self.message_service_choices.get(
                raw_data.get("X-Service")),
            external_id=raw_data.get("X-External-Id"),
            recipient=raw_data.get("X-Sender")[:13],
            message_status=self.message_status_choices.get(
                raw_data.get("X-Status")),
            payload=data
        )
        return Response(data={"message": "Success"}, status=status.HTTP_201_CREATED)


class RouteDlrAPIView(APIView):
    serializer_class = MessageStatusSerializer

    def post(self, request):
        data = {}
        message_id = str(datetime.now())

        data["description"] = request.POST.get("sStatus").upper()
        data["status"] = request.POST.get("sStatus").upper()
        data["sender_id"] = request.POST.get("sStatus").upper()
        data["bulkId"] = request.POST.get("bulkId", "")
        data["price"] = request.POST.get("iCostPerSms", "")
        data["account_balance"] = request.POST.get("account_balance", "empty")
        data["timestamp"] = request.POST.get("dtDone", "")
        data["event_timestamp"] = request.POST.get("dtSubmit", "")
        data["sms_id"] = request.POST.get("sMessageId", "")
        data["ref_id"] = request.POST.get("sMessageId", "")
        data["to"] = request.POST.get("sMobileNo", "")
        data["source"] = "ROUTE"
        raw_data = json.dumps(data)
        data["raw_status"] = raw_data

        connect_route_database.set(message_id, raw_data)

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            data = {
                'status': True,
                'message': 'Successful',
                'data': serializer.data
            }
            return JsonResponse(data=data, status=status.HTTP_201_CREATED)


class DotgoDlrAPIView(APIView):
    serializer_class = MessageStatusSerializer

    def post(self, request):
        try:
            message_id = str(datetime.now())

            data = json.loads(request.data)
            print(
                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n    !!DATA!!      {data}      !!DATA!!     \n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            )
            data["sender_id"] = data.get("id", "")
            data["sms_id"] = data.get("ref_id", "")
            data["price"] = data.get("price", "empty")
            data["account_balance"] = data.get("account_balance", "empty")
            data["raw_status"] = "{}"  # str(data)
            data["ref_id"] = data.get("id", "")
            raw_data = json.dumps(data)

            connect_dotgo_database(message_id, raw_data)

            serializer = self.serializer_class(data=data)

            serializer.is_valid(raise_exception=True)
            print(
                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n          ATTEMPTING TO SAVE CALLBACK           \n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            )
            serializer.save()

            print(
                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n          CALLBACK    SAVED       ALREADY           \n\n\n\n\n\n\n\n\n\n\n\n\n\n"
            )

            data = {
                'status': True,
                'message': 'Successful',
                'data': serializer.data
            }
            response = "ok"
        except Exception as error:

            response = str(traceback.format_exc()), str(error)

        return Response({"response": response}, status=status.HTTP_201_CREATED)


class InfobipDlrAPIView(APIView):
    serializer_class = MessageStatusSerializer

    def post(self, request):
        message_id = str(datetime.now())

        data = json.loads(request.body)
        data = request.data.get("results")[0]

        data["description"] = data['status']['groupName'].upper()
        data["status"] = data["status"]['name'].upper()
        data["sender_id"] = data.get("id", "-")
        data["bulkId"] = data.get("bulkId", "")
        data["price"] = data.get("price", "").get("pricePerMessage")
        data["account_balance"] = data.get("account_balance", "empty")
        data["raw_status"] = str(data)
        data["timestamp"] = data.get("doneAt", "")
        data["event_timestamp"] = data.get("doneAt", "")
        data["sms_id"] = data.get("messageId", "")
        data["ref_id"] = data.get("bulkId", "")
        data["source"] = "INFOBIP"

        raw_data = json.dumps(data)

        connect_infobip_database.set(message_id, raw_data)

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            data = {
                'status': True,
                'message': 'Successful',
                'data': serializer.data
            }
            return JsonResponse(data=data, status=status.HTTP_201_CREATED)


class RouteTwoDlrAPIView(APIView):
    serializer_class = MessageStatusSerializer

    def post(self, request):
        data = {}
        message_id = str(datetime.now())

        data["description"] = request.POST.get("sStatus").upper()
        data["status"] = request.POST.get("sStatus").upper()
        data["sender_id"] = request.POST.get("sStatus").upper()
        data["bulkId"] = request.POST.get("bulkId", "")
        data["price"] = request.POST.get("iCostPerSms", "")
        data["account_balance"] = request.POST.get("account_balance", "empty")
        data["timestamp"] = request.POST.get("dtDone", "")
        data["event_timestamp"] = request.POST.get("dtSubmit", "")
        data["sms_id"] = request.POST.get("sMessageId", "")
        data["ref_id"] = request.POST.get("sMessageId", "")
        data["to"] = request.POST.get("sMobileNo", "")
        data["source"] = "ROUTE_TRANS"
        raw_data = json.dumps(data)
        data["raw_status"] = raw_data

        connect_route_database.set(message_id, raw_data)

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            data = {
                'status': True,
                'message': 'Successful',
                'data': serializer.data
            }
            return JsonResponse(data=data, status=status.HTTP_201_CREATED)
