"""
file_name = events.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/30/2023
Description: A file used to get events data then format it
Edit Log: 
07/30/2023 
    - Moved over file from original tool receiver
"""

from argparse import Namespace
from datetime import datetime
from os import getenv

from requests import post
from stringcolor import cs as color

from utils.request_handshake import RequestHandshake
from utils.timer import Timer


def setup_default_event_request(base_request: dict, args: Namespace) -> dict:
    """
    Set up the default event request dictionary.

    Args:
        base_request `dict``: The base request dictionary.
        args `Namespace``: The namespace object containing parsed command-line arguments.

    Returns:
        `dict`: The updated base request dictionary.
    """

    base_request["defaultForm"] = {"DefaultOption": args.default}
    base_request["stringifyResult"] = True

    return base_request


@Timer(print_time=True, print_response=False)
@RequestHandshake()
def get_default_events(args: Namespace) -> None:
    """
    Get default events.

    This function retrieves default events using an API and prints them to the console.

    Args:
        args `Namespace`: The namespace object containing parsed command-line arguments.
    """

    base_request = setup_default_event_request(
        RequestHandshake.base_request.copy(), args
    )
    results = post(
        url=f"{getenv('TOOLS_URL')}/getEvent", json=base_request, timeout=5
    ).json()

    if not results:
        print(f"{color(f'No events scheduled for {args.default}', 'grey4')}")
    else:
        weekday: str = datetime.today().strftime("%A") + "'s Schedule"
        print(f"{color(weekday, 'grey4')}")
        for result in results:
            print(result)
