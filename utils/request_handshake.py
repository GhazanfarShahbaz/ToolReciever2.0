"""
file_name = request_handshake.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/30/2023
Description: A file used to create a handshake decorator and context manger
    for functions
Edit Log: 
07/30/2023 
    - Created file, speed up from the original tool receiver by almost 100%
"""

from firebase_admin import firestore

from utils.firestore_utils import get_base_request, update_firestore_login

class RequestHandshake:
    """
    A class that represents a handshake for making requests.
    """

    base_request: dict = get_base_request()

    def __init__(self):
        """
        Initialize a new instance of RequestHandshake class.
        """

        self.fs_database = firestore.client()

    def __enter__(self) -> "RequestHandshake":
        """
        Enter the context manager.

        Returns:
            `RequestHandshake`:
                The current instance of `RequestHandshake`.
        """

        update_firestore_login(self.fs_database, True)

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

        update_firestore_login(self.fs_database, False)

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

            update_firestore_login(self.fs_database, True)
            return func(*args, **kwargs)
            # We do not need to close the connection, the server will do that for us

        return wrapper
