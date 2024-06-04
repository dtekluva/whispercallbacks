from requests import exceptions, request


# Create reusable functions and objects.
def make_request(request_type: str, params: dict) -> dict:
    """
    Make an HTTP request using the specified request_type and parameters.
    Args:
        request_type (str): The type of HTTP request to make (e.g., 'GET', 'POST', 'PUT', 'DELETE', etc.).
        params (dict): A dictionary containing the parameters to be passed in the HTTP request.
    Returns:
        dict: A dictionary containing the response status, data, and error details.
        - 'status': A boolean indicating if the request was successful (True) or not (False).
        - 'data': A dictionary containing the JSON response data if the request was successful, otherwise None.
        - 'error': A dictionary containing error details if the request failed, otherwise None.
    """
    try:
        response = request(request_type, **params)
        try:
            data = response.json()
        except exceptions.JSONDecodeError:
            data = response.text
        return {
            "status_code": response.status_code,
            "status": True,
            "data": data,
            "error": None,
        }
    except exceptions.RequestException as error:
        return {
            "status_code": "07",
            "status": False,
            "data": None,
            "error": str(error),
        }
