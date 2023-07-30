"""
file_name = reload_token.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/29/2023
Description: A file used to reload and check the status of the credential token
Edit Log: 
07/29/2023 
    - Moved over file from original tool receiver
    - Better formatted and documented code
"""

import os

from datetime import datetime
from json import load, dump

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import (
    InstalledAppFlow,
    Flow,
)


def check_update_json() -> bool:
    """
    Checks the update json to see if it the credential json has been updated with the last week

    Returns:
        `bool`: True if the update json has been updated with the last week, otherwise false
    """
    last_updated: datetime = None

    with open(os.getenv("UPDATED_JSON_PATH"), encoding="UTF-8") as updated_json:
        data = load(updated_json)

        last_updated = datetime.strptime(data["last_updated"], "%Y-%m-%d %H:%M:%S.%f")

    return (datetime.now() - last_updated).days < 7


def reload(
    scopes: list,
    token_file_name=os.getenv("TOKEN_PATH"),
    credential_file_name=os.getenv("CREDENTIALS_PATH"),
) -> None:
    """
    Reloads the google token and updates the json file with the
    current date if the credential file needs to be updated

    Args:
        scopes `list` : A list of google scopes

        token_file_name `str` : The path to the token file. Defaults to env

        credential_file_name `str` : The path to credentials file. Defaults to env
    """

    credentials: Credentials | None = (
        Credentials.from_authorized_user_file(token_file_name, scopes=scopes)
        if os.path.exists(token_file_name)
        else None
    )

    if credentials and (credentials.valid or check_update_json()):
        return

    flow: Flow = InstalledAppFlow.from_client_secrets_file(credential_file_name, scopes)
    credentials = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(file=token_file_name, mode="w", encoding="UTF-8") as token:
        token.write(credentials.to_json())

    with open(
        file=os.getenv("UPDATED_JSON_PATH"), mode="w", encoding="UTF-8"
    ) as updated_json:
        dump({"last_updated": datetime.now()}, updated_json, default=str)
