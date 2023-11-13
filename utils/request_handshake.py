"""
file_name = request_handshake.py
Created On: 2023/11/12
Lasted Updated: 2023/11/12
Description: _FILL OUT HERE_
Edit Log:
2023/11/12
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from os import getenv
from json import load, dump

# THIRD PARTY LIBRARY IMPORTS
from requests import post


# LOCAL LIBRARY IMPORTS
from utils.firestore_utils import get_base_request


def get_authentication_base_request() -> dict:
    """
    Gets the authentication base request.

    If authentication is not stale then returns quick,
    otherwise requests for a new one and updates the cache.

    Returns:
        dict:   A dictionary representing the authentication base request it
                contains a username and a token.
    """

    def read_cache() -> dict:
        data = {}

        with open(getenv("HANDSHAKE_CACHE_PATH"), encoding="UTF-8") as updated_json:
            data = load(updated_json)

        return data

    def save_cache(handshake_cache) -> None:
        with open(
            file=getenv("HANDSHAKE_CACHE_PATH"), mode="w", encoding="UTF-8"
        ) as token:
            dump(handshake_cache, token, default=str)

    try:
        validation_json = post(
            url=f"{getenv('TOOLS_URL')}/validateAuthenticationToken",
            json=read_cache(),
            timeout=5,
        ).json()

        if validation_json["ErrorCode"] == 0:
            return validation_json

    except Exception as exception:  # pylint: disable=broad-exception-caught
        print("Old cache stale, getting new token", exception)

    base_request = get_base_request()

    authentication_json = post(
        url=f"{getenv('TOOLS_URL')}/grantAuthenticationToken",
        json=get_base_request(),
        timeout=5,
    ).json()

    handshake_json = {
        "username": base_request["username"],
        "token": authentication_json["token"],
    }

    save_cache(handshake_json)

    return handshake_json


class RequestHandshake:
    """
    A class that represents a handshake for making requests.
    """

    base_request = get_authentication_base_request()

    def __init__(self):
        """
        Initialize a new instance of RequestHandshake class.
        """

    def __enter__(self) -> "RequestHandshake":
        """
        Enter the context manager.

        Returns:
            `RequestHandshake`:
                The current instance of `RequestHandshake`.
        """

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exit the context manager.

        Args:
            exc_type:
                The type of the exception.
            exc_val:
                The value of the exception.
            exc_tb:
                The traceback of the exception.
        """

    def __call__(self, func):
        """
        Decorator function.

        Args:
            func: The function to be decorated.

        Returns:
            function: The decorated function.
        """

        def wrapper(*args, **kwargs):
            """
            Wrapper function that opens up the server to requests.

            Args:
                *args:
                    Variable length argument list.
                **kwargs:
                    Arbitrary keyword arguments.

            Returns:
                any:
                    The result of the decorated function call.
            """

            return func(*args, **kwargs)
            # We do not need to close the connection, the server will do that for us

        return wrapper
