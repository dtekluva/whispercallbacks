import json

from celery import shared_task

from helpers.redis_db import (
    connect_dotgo_database,
    connect_exchange_database,
    connect_infobip_database,
    connect_route_database,
    connect_smartsms_database,

)
from helpers.reusable import make_request


HEADERS = {
    "Content-type": "application/json"
}

WHISPERSMS_DOTGO_URL = "https://whispersms.xyz/whisper/sms_callback_v2/"
WHISPERSMS_EXCHANGE_TELECOM_URL = "https://whispersms.xyz/whisper/sms_callback_exchange/"
WHISPERSMS_INFOBIP_URL = "https://whispersms.xyz/whisper/sms_callback_infobip_v2/"
WHISPERSMS_ROUTE_URL = "https://whispersms.xyz/whisper/sms_callback_route_v2/"
WHISPERSMS_SMARTSMS_URL = "https://whispersms.xyz/whisper/sms_callback_smartsms/"


# Create your task(s) here.
@shared_task
def send_exchange_telecom_callback():
    available_keys = connect_exchange_database.keys("*")

    if available_keys:
        available_data = [
            connect_exchange_database.get(key) for key in available_keys
        ]
        for data in available_data:
            raw_data = json.loads(data)
            payload = json.dumps(raw_data)

            response = make_request(
                "POST", dict(
                    url=WHISPERSMS_EXCHANGE_TELECOM_URL,
                    headers=HEADERS,
                    data=payload
                )
            )
        connect_exchange_database.delete(*available_keys)
        return "CALLBACK SENT SUCCESSFULLY"
    else:
        return "NO DATA AVAILABLE !"


@shared_task
def send_route_callback():
    available_keys = connect_route_database.keys("*")

    if available_keys:
        available_data = [
            connect_route_database.get(key) for key in available_keys
        ]
        for data in available_data:
            raw_data = json.loads(data)
            payload = json.dumps(raw_data)

            response = make_request(
                "POST", dict(
                    url=WHISPERSMS_ROUTE_URL,
                    headers=HEADERS,
                    data=payload
                )
            )
        connect_route_database.delete(*available_keys)
        return "CALLBACK SENT SUCCESSFULLY"
    else:
        return "NO AVAILABLE DATA !"


@shared_task
def send_dotgo_callback():
    available_keys = connect_dotgo_database.keys("*")

    if available_keys:
        available_data = [
            connect_dotgo_database.get(key) for key in available_keys
        ]
        for data in available_data:
            raw_data = json.loads(data)
            payload = json.dumps(raw_data)

            response = make_request(
                "POST", dict(
                    url=WHISPERSMS_DOTGO_URL,
                    headers=HEADERS,
                    data=payload
                )
            )
        connect_dotgo_database.delete(*available_keys)
        return "CALLBACK SENT SUCCESSFULLY"
    else:
        return "NO AVAILABLE DATA !"


@shared_task
def send_infobip_callback():
    available_keys = connect_infobip_database.keys("*")

    if available_keys:
        available_data = [
            connect_infobip_database.get(key) for key in available_keys
        ]
        for data in available_data:
            raw_data = json.loads(data)
            payload = json.dumps(raw_data)

            response = make_request(
                "POST", dict(
                    url=WHISPERSMS_INFOBIP_URL,
                    headers=HEADERS,
                    data=payload
                )
            )
        connect_infobip_database.delete(*available_keys)
        return "CALLBACK SENT SUCCESSFULLY"
    else:
        return "NO AVAILABLE DATA !"


@shared_task
def send_smartsms_callback():
    available_keys = connect_smartsms_database.keys("*")

    if available_keys:
        available_data = [
            connect_smartsms_database.get(key) for key in available_keys
        ]
        for data in available_data:
            raw_data = json.loads(data)
            payload = json.dumps(raw_data)

            response = make_request(
                "POST", dict(
                    url=WHISPERSMS_SMARTSMS_URL,
                    headers=HEADERS,
                    data=payload
                )
            )
        connect_smartsms_database.delete(*available_keys)
        return "CALLBACK SENT SUCCESSFULLY"
    else:
        return "NO AVAILABLE DATA !"
