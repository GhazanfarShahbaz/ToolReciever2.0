"""
file_name = diagnostics.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/30/2023
Description: A file used to endpiont diagnostics
Edit Log: 
07/30/2023 
    - Moved over file from original tool receiver
"""

from argparse import Namespace
from datetime import datetime
from os import getenv
from typing import List

from stringcolor import cs as color
from requests import post
from termplotlib import figure


from utils.request_handshake import RequestHandshake
from utils.timer import Timer


def setup_diagnostics_request(base_request: dict, args: Namespace) -> dict:
    """
    Set up the default diagnostics request dictionary.

    Args:
        base_request `dict``: The base request dictionary.
        args `Namespace``: The namespace object containing parsed command-line arguments.

    Returns:
        `dict`: The updated base request dictionary.
    """

    todays_date: datetime = datetime.now()
    start_date, end_date = None, None

    if args.diagnostics == "today":
        start_date = datetime(
            todays_date.year, todays_date.month, todays_date.day, 0, 0, 0
        )
        end_date = datetime(
            todays_date.year, todays_date.month, todays_date.day, 23, 59, 59
        )
    elif args.diagnostics == "month":
        start_date = datetime(
            todays_date.year,
            todays_date.month - 1 if todays_date.month > 1 else 12,
            todays_date.day,
            23,
            59,
            59,
        )
        end_date = datetime(
            todays_date.year, todays_date.month, todays_date.day, 23, 59, 59
        )
    elif args.diagnostics == "year":
        start_date = datetime(
            todays_date.year - 1, todays_date.month, todays_date.day, 23, 59, 59
        )
        end_date = datetime(
            todays_date.year, todays_date.month, todays_date.day, 23, 59, 59
        )

    base_request["filterForm"] = {
        "EndpointCounter": True,
        "DateFrom": start_date.strftime("%m/%d/%y %H:%M"),
        "DateTo": end_date.strftime("%m/%d/%y %H:%M"),
    }

    return base_request


@Timer(print_time=True, print_response=False)
@RequestHandshake()
def get_diagnostics(args: Namespace) -> None:
    """
    Get diagnostics.

    This function retrieves diagnostics using an API and prints them to the console.

    Args:
        args `Namespace`: The namespace object containing parsed command-line arguments.
    """
    base_request: dict = setup_diagnostics_request(
        RequestHandshake.base_request.copy(), args
    )
    results = post(
        url=f"{getenv('TOOLS_URL')}/getEndpointDiagnostics",
        json=base_request,
        timeout=5,
    ).json()

    values: List[str] = list(results.values())
    keys: List[int] = list(results.keys())

    if len(values) == 0:
        print(f"{color('No endpoints hit yet', 'grey4')}")
    else:
        print(f"{color('Endpoints Hit Count ({args.diagnostics})', 'grey4')}")
        fig = figure()
        fig.barh(values, keys, force_ascii=True)
        fig.show()

    print()
