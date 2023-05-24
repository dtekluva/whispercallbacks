import json

from django.core.management.base import BaseCommand

from callbacks.models import MessageStatus
from callbacks.tasks import HEADERS, WHISPERSMS_ROUTE_URL
from helpers.reusable import make_request


# Update existing message status(es).
class Command(BaseCommand):
    help = 'UPDATES ALL EXISTING MESSAGE STATUSES'

    def handle(self, *args, **kwargs):
        statuses = MessageStatus.objects.filter(
            source="ROUTE"
        )

        for status in statuses:
            data = {
                "description": status.status,
                "status": status.status,
                "sender_id": status.sender_id,
                "bulkId": status.ref_id,
                "price": status.price,
                "account_balance": status.account_balance,
                "timestamp": status.timestamp,
                "event_timestamp": status.event_timestamp,
                "sms_id": status.sms_id,
                "ref_id": status.ref_id,
                "to": status.to,
                "source": status.source
            }

            payload = json.dumps(data)

            response = make_request(
                "POST", dict(
                    url=WHISPERSMS_ROUTE_URL,
                    headers=HEADERS,
                    data=payload
                )
            )
            print(response)

        print("T H E  J O B  I S  D O N E ! ! ! !")
