import json

from celery import shared_task

from helpers.redis_db import (
    connect_dotgo_database,
    connect_exchange_database,
    connect_infobip_database,
    connect_route_database,
    connect_smartsms_database,
    connect_broadbased_database,
)
from helpers.reusable import make_request


HEADERS = {"Content-type": "application/json"}

WHISPERSMS_DOTGO_URL = "https://whispersms.xyz/whisper/sms_callback_v2/"
WHISPERSMS_EXCHANGE_TELECOM_URL = (
    "https://whispersms.xyz/whisper/sms_callback_exchange/"
)
WHISPERSMS_INFOBIP_URL = "https://whispersms.xyz/whisper/sms_callback_infobip_v2/"
WHISPERSMS_ROUTE_URL = "https://whispersms.xyz/whisper/sms_callback_route_v2/"
WHISPERSMS_SMARTSMS_URL = "https://whispersms.xyz/whisper/sms_callback_smartsms/"
WHISPERSMS_BROADBASED_URL = "https://whispersms.xyz/whisper/sms_callback_broadbased/"


# Create your task(s) here.
@shared_task
def send_exchange_telecom_callback():
    """
    Response code == 201
    """
    available_keys = connect_exchange_database.keys("*")
    if available_keys:
        for key in available_keys:
            value = connect_exchange_database.get(key)
            raw_data = json.loads(value)
            payload = json.dumps(raw_data)
            response = make_request(
                "POST",
                dict(
                    url=WHISPERSMS_EXCHANGE_TELECOM_URL,
                    headers=HEADERS,
                    data=payload,
                ),
            )
            if response.get("status_code") == 201:
                connect_exchange_database.delete(key)
        return "SUCCESSFULLY FORWARDED EXCHANGE TELECOM DLRs."
    else:
        return "NO PENDING EXCHANGE TELECOM DLRs."


@shared_task
def send_route_callback():
    """
    Response code == 201
    """
    available_keys = connect_route_database.keys("*")
    if available_keys:
        for key in available_keys:
            value = connect_route_database.get(key)
            raw_data = json.loads(value)
            payload = json.dumps(raw_data)
            response = make_request(
                "POST",
                dict(
                    url=WHISPERSMS_ROUTE_URL,
                    headers=HEADERS,
                    data=payload,
                ),
            )
            if response.get("status_code") == 201:
                connect_route_database.delete(key)
        return "SUCCESSFULLY FORWARDED ROUTE MOBILE DLRs."
    else:
        return "NO PENDING ROUTE MOBILE DLRs."


@shared_task
def send_dotgo_callback():
    """
    Response code == 201
    """
    available_keys = connect_dotgo_database.keys("*")
    if available_keys:
        for key in available_keys:
            value = connect_dotgo_database.get(key)
            raw_data = json.loads(value)
            payload = json.dumps(raw_data)
            response = make_request(
                "POST",
                dict(
                    url=WHISPERSMS_DOTGO_URL,
                    headers=HEADERS,
                    data=payload,
                ),
            )
            if response.get("status_code") == 201:
                connect_dotgo_database.delete(key)
        return "SUCCESSFULLY FORWARDED DOTGO DLRs."
    else:
        return "NO PENDING DOTGO DLRs."


@shared_task
def send_infobip_callback():
    """
    Response code == 201
    """
    available_keys = connect_infobip_database.keys("*")
    if available_keys:
        for key in available_keys:
            value = connect_infobip_database.get(key)
            raw_data = json.loads(value)
            payload = json.dumps(raw_data)
            response = make_request(
                "POST",
                dict(
                    url=WHISPERSMS_INFOBIP_URL,
                    headers=HEADERS,
                    data=payload,
                ),
            )
            if response.get("status_code") == 201:
                connect_infobip_database.delete(key)
        return "SUCCESSFULLY FORWARDED INFOBIP DLRs."
    else:
        return "NO PENDING INFOBIP DLRs."


@shared_task
def send_smartsms_callback():
    available_keys = connect_smartsms_database.keys("*")
    if available_keys:
        for key in available_keys:
            value = connect_smartsms_database.get(key)
            raw_data = json.loads(value)
            payload = json.dumps(raw_data)
            response = make_request(
                "POST",
                dict(
                    url=WHISPERSMS_SMARTSMS_URL,
                    headers=HEADERS,
                    data=payload,
                ),
            )
            if response.get("status_code") == 201:
                connect_smartsms_database.delete(key)
        return "SUCCESSFULLY FORWARDED SMARTSMS DLRs."
    else:
        return "NO PENDING SMARTSMS DLRs."


@shared_task
def send_broadbased_callback():
    available_keys = connect_broadbased_database.keys("*")
    if available_keys:
        for key in available_keys:
            value = connect_broadbased_database.get(key)
            raw_data = json.loads(value)
            payload = json.dumps(raw_data)
            response = make_request(
                "POST",
                dict(
                    url=WHISPERSMS_BROADBASED_URL,
                    headers=HEADERS,
                    data=payload,
                ),
            )
            if response.get("status_code") == 201:
                connect_broadbased_database.delete(key)
        return "SUCCESSFULLY FORWARDED BROADBASED DLRs."
    else:
        return "NO PENDING BROADBASED DLRs."
