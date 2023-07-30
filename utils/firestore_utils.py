"""
file_name = firestore_utils.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/30/2023
Description: A file used to interact with firestore
Edit Log: 
07/30/2023 
    - Moved over file from original tool receiver
    - Modularized preexisting code from original tool receiver
    - Remove global variable with static class variable
"""

from os import getenv
from typing import Union

from firebase_admin import credentials, firestore, initialize_app

from utils.reload_token import reload


CREDENTIALS: Union[str, None] = credentials.Certificate(getenv("FIRESTORE_PATH"))
initialize_app(CREDENTIALS)

def get_base_request() -> dict:
    """Returns the base request for the server

    Returns:
        `dict``: A base request containing the username and password to the server
    """

    if not hasattr(get_base_request, "base_request"):
        get_base_request.base_request: Union[dict, None] = None

    if not get_base_request.base_request:
        reload(
            [
                "https://www.googleapis.com/auth/gmail.readonly",
                "https://www.googleapis.com/auth/gmail.modify",
                "https://www.googleapis.com/auth/calendar.readonly",
            ]
        )

    if not get_base_request.base_request:
        fs_database = firestore.client()
    
        users_ref = (
            fs_database.collection(getenv("FIRESTORE_SERVER"))
            .document(getenv("FIRESTORE_DOC_ID"))
            .get()
        )

        get_base_request.base_request = users_ref.to_dict()

    return get_base_request.base_request


def update_firestore_login(fs_database: any, allow_login: bool) -> None:
    """
    Update the Firestore login status.

    Args:
        fs_database `any`: The Firestore database. If not provided, a new client will be created.

        allow_login `bool`: The new value for the login status.
    """

    if not fs_database:
        fs_database = firestore.client()

    login_allow = fs_database.collection(getenv("FIRESTORE_SERVER")).document("allow")

    # change only only if allow_login is different from current value
    if login_allow.get().to_dict()["allow"] is not allow_login:
        login_allow.update({"allow": allow_login})
