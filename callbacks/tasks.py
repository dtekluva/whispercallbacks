import json
import redis
from celery import shared_task

from helpers.reusable import make_request


WHISPERSMS_EXCHANGE_TELECOM_URL = "https://whispersms.xyz/whisper/sms_callback_exchange/"


# Create your task(s) here.
@shared_task
def send_exchange_telecom_callback():
    url = WHISPERSMS_EXCHANGE_TELECOM_URL
    headers = {
        "Content-type": "application/json"
    }

    redis_database = redis.StrictRedis(
        host="localhost", port=6379, db=4, decode_responses=True
    )
    available_keys = redis_database.keys("*")

    if available_keys:
        available_data = [
            redis_database.get(key) for key in available_keys
        ]
        for data in available_data:
            payload = json.dumps(data)
            response = make_request(
                "POST", dict(
                    url=url,
                    headers=headers,
                    data=payload
                )
            )
            print(response)
            if response.get("message") == "Success":
                redis_database.delete(*available_keys)
    else:
        print("NO AVAILABLE DATA !")
