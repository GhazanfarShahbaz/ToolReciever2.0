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

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS
from utils.firestore_utils import get_authentication_base_request


class RequestHandshake:
    """
    A class that represents a handshake for making requests.
    """

    base_request = (  # pylint: disable=bad-classmethod-argument
        get_authentication_base_request()
    )

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

    @classmethod
    def __call__(self, func):  # pylint: disable=bad-classmethod-argument
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

            # update request if needed
            base_request = (  # pylint: disable=unused-variable
                get_authentication_base_request()
            )

            return func(*args, **kwargs)
            # We do not need to close the connection, the server will do that for us

        return wrapper
