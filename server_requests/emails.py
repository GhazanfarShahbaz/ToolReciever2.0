"""
file_name = emails.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/30/2023
Description: A file used to get email data then format it
Edit Log: 
07/30/2023 
    - Moved over file from original tool receiver
"""
from os import getenv

from requests import post
from stringcolor import cs as color

from utils.firestore_utils import read_token_file
from utils.request_handshake import RequestHandshake
from utils.timer import Timer


def setup_default_event_request(base_request: dict) -> dict:
    """
    Set up the default event request dictionary.

    Args:
        base_request `dict``: The base request dictionary.
        args `Namespace``: The namespace object containing parsed command-line arguments.

    Returns:
        `dict`: The updated base request dictionary.
    """

    base_request["authorizationFile"] = read_token_file()
    base_request["labelFilters"] = ["IMPORTANT"]
    base_request["maxResults"] = 5
    base_request["snippet"] = True

    return base_request

@Timer(print_time=True, print_response=False)
@RequestHandshake()
def get_default_emails() -> None:
    base_request: dict = setup_default_event_request(RequestHandshake.base_request.copy())
    results = post(
            url=f"{getenv('TOOLS_URL')}/getGmailEmails",
            json=base_request,
            timeout=5
    ).json()
    
    print(f"{color('Emails', 'grey4')}")
    for key, result in results.items():
        print(color("Labels " + " ".join(result["Labels"]), "dodgerblue"))
        if "Subject" in result.keys():
            print(
                f"{color(result['Sender'], 'grey1')} {color(result['Subject'], 'black')}"
            )
        print(f"{color(result['Snippet'].strip(), 'yellow')}")
        print()