import json, traceback

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from call_backs.helpers.rest_framework import PlainTextParser
from call_backs.models import *
from call_backs.serializers import *


# Create your view(s) here.
@api_view(['GET', 'POST'])
@parser_classes([JSONParser, PlainTextParser])
def dotgo_sms_callback(request):

    if request.method == 'GET':
        message_statuses = DotgoCallback.objects.all()
        serializer = DotgoStatusSerializer(message_statuses, many=True)

        data = {
            "status": True,
            "message": "Successful",
            "data": serializer.data,
            "count": len(serializer.data)
        }

        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # print(request.POST)
        # print(request.data)

        try:
            data = json.loads(request.data)
            data["sender_id"] = data.get("id", "")
            data["sms_id"] = data.get("ref_id", "")
            data["price"] = data.get("price", "empty")
            data["account_balance"] = data.get("account_balance", "empty")
            data["raw_status"] = "{}" # str(data)
            data["ref_id"] = data.get("id", "")

            serializer = DotgoStatusSerializer(data=data)

            # print(data)

            if serializer.is_valid():
                serializer.save()

                # Message.subsequent_dotgo_update(data)

                data = {
                    'status': True,
                    'message': 'Successful',
                    'data': serializer.data
                }

                response = "ok"

        except Exception as e:

            response = str(traceback.format_exc()), str(e)

        return Response({"response": response}, status=status.HTTP_201_CREATED)

        # else:
        #     data = {
        #         'status': False,
        #         'message': 'Unsuccessful',
        #         'error': serializer.errors
        #     }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@parser_classes([JSONParser])
@csrf_exempt
def route_sms_callback(request):

    if request.method == 'GET':
        message_statuses = RouteCallback.objects.all()
        serializer = RouteStatusSerializer(message_statuses, many=True)

        data = {
            "status": True,
            "message": "Successful",
            "data": serializer.data,
            "count": len(serializer.data)
        }
        return HttpResponse(data, status=status.HTTP_200_OK)

    elif request.method == 'POST':


        # data = request.data.get("results")[0]
        # print(request.POST)
        data = {}
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
        data["raw_status"] = json.dumps(data)

        serializer = RouteStatusSerializer(data=data)
        # Message.subsequent_route_update(data)

        if serializer.is_valid():

            serializer.save()

            data = {
                'status': True,
                'message': 'Successful',
                'data': serializer.data
            }
        else:
            data = {
                'status': True,
                'message': 'Successful',
                'data': serializer.errors
            }

        return JsonResponse(data, status=status.HTTP_201_CREATED)
