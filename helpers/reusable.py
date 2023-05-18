from requests import exceptions, request


# Create reusable functions and objects.
def make_request(request_type: str, params: dict) -> dict:
    try:
        response = request(request_type, **params)
        return response.json()
    except exceptions.RequestException as error:
        return {
            "error": "WhisperSMS Request Broken",
            "message": f"{error}"
        }
