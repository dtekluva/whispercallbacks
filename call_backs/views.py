from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from call_backs.models import ExchangeTelecomDlr


# Create your view(s) here.
class ExchangeTelecomDlrAPIView(APIView):

    def post(self, request):
        """
        DLR is sent via request headers.
        """

        ExchangeTelecomDlr.objects.create(payload=request.headers)
        return Response(data={"message": "Success"}, status=status.HTTP_201_CREATED)
