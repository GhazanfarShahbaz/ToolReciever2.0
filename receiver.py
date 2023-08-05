"""
file_name = receiver.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/30/2023
Description: Used to setup arguments for the argparser and call the functions
Edit Log: 
07/30/2023 
    - Created new receiver file
    - Added weather argument
    - Added total execution time
08/04/2023
    - Added logs argument
"""

from argparse import ArgumentParser, Namespace
from typing import Dict, Callable

from utils.timer import Timer

from server_requests.diagnostics import get_diagnostics
from server_requests.emails import get_default_emails
from server_requests.events import get_default_events
from server_requests.logs import get_logs
from server_requests.weather import get_weather

PARSER: ArgumentParser = ArgumentParser()


# ARGUMENTS
PARSER.add_argument(
    "-df",
    "--default",
    help="Filter events by default options: today, weekly, month or year",
    type=str,
)

PARSER.add_argument(
    "-dgm",
    "--dgmail",
    help="Get a list of default email snippets",
    action="store_true",
)

PARSER.add_argument(
    "-diagnostics", "--diagnostics", help="Show endpoint diagnostics", type=str
)

PARSER.add_argument("-gl", "--getlogs", help="Get today's Logs", action="store_true")

PARSER.add_argument("-w", "--weather", help="Get todays weather", action="store_true")


# FUNCTION MAPPING
ARG_TO_FUNCTION: Dict[str, Dict[str, any]] = {
    "default": {"function": get_default_events, "pass_args": True},
    "dgmail": {"function": get_default_emails, "pass_args": False},
    "diagnostics": {"function": get_diagnostics, "pass_args": True},
    "getlogs": {"function": get_logs, "pass_args": False},
    "weather": {"function": get_weather, "pass_args": False},
}


if __name__ == "__main__":
    args: Namespace = PARSER.parse_args()

    for arg in vars(args):
        if getattr(args, arg) and ARG_TO_FUNCTION.get(arg):
            arg_method: Callable = ARG_TO_FUNCTION[arg]["function"]

            if ARG_TO_FUNCTION[arg]["pass_args"]:
                arg_method(args)
            else:
                arg_method()

    Timer().print_and_format_time("Total Time:")
