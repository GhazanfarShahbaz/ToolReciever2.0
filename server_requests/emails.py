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
    """
    Retrieves emails based on default options.
    This function makes an API request to get emails data and prints it to the console.

    Note:
        The `print_time` parameter of the `Timer` decorator is set to True,
        which prints the execution time of the function.
        The `print_response` parameter of the `Timer` decorator is set to False,
            which suppresses the printing of the function response.

    Raises:
        HTTPError: If there is an error occurred during the API request.
    """

    base_request: dict = setup_default_event_request(RequestHandshake.base_request.copy())
    results = post(
            url=f"{getenv('TOOLS_URL')}/getGmailEmails",
            json=base_request,
            timeout=5
    ).json()

    print(f"{color('Emails', 'grey4')}")
    for result in results.values():
        print(color("Labels " + " ".join(result["Labels"]), "dodgerblue"))
        if "Subject" in result.keys():
            print(
                f"{color(result['Sender'], 'grey1')} {color(result['Subject'], 'black')}"
            )
        print(f"{color(result['Snippet'].strip(), 'yellow')}")
