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
from typing import Dict, List, Callable
from sys import argv

from utils.timer import Timer

from server_requests.coding_questions import (
    get_random_codechef_question,
    get_random_leetcode_question,
    get_random_euler_question,
)
from server_requests.diagnostics import get_diagnostics
from server_requests.emails import get_default_emails
from server_requests.events import get_default_events
from server_requests.logs import get_logs
from server_requests.weather import get_weather

PARSER: ArgumentParser = ArgumentParser()


# ARGUMENTS

# CODECHEF + ARGUMENTS
PARSER.add_argument(
    "-cf", "--codechef", help="Get a codechef question", action="store_true"
)
PARSER.add_argument(
    "-cf_d", "--cf_difficulty", help="Filter codechef by a difficulty", type=str
)

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

PARSER.add_argument("-euler", "--euler", help="Get a random euler question", type=str)

PARSER.add_argument("-gl", "--getlogs", help="Get today's Logs", action="store_true")

# LEETCODE + ARGUMENTS
PARSER.add_argument(
    "-lc", "--leetcode", help="Get a leetcode question", action="store_true"
)
PARSER.add_argument(
    "-lc_d", "--lc_difficulty", help="Filter leetcode by a difficulty", type=str
)
PARSER.add_argument("-lc_t", "--lc_tag", help="Filter leetcode by a tag", type=str)

PARSER.add_argument("-w", "--weather", help="Get todays weather", action="store_true")


# FUNCTION MAPPING
ARG_TO_FUNCTION: Dict[str, Dict[str, any]] = {
    "codechef": {"function": get_random_codechef_question, "pass_args": True},
    "default": {"function": get_default_events, "pass_args": True},
    "dgmail": {"function": get_default_emails, "pass_args": False},
    "diagnostics": {"function": get_diagnostics, "pass_args": True},
    "euler": {"function": get_random_euler_question, "pass_args": False},
    "getlogs": {"function": get_logs, "pass_args": False},
    "leetcode": {"function": get_random_leetcode_question, "pass_args": True},
    "weather": {"function": get_weather, "pass_args": False},
}


def argument_parser(args: List[str]) -> None:
    """Parse command-line arguments and call corresponding functions.

    Args:
        args (List[str]): A list of command-line arguments.

    Returns:
        None
    """

    args: Namespace = PARSER.parse_args(args)

    for arg in vars(args):
        if getattr(args, arg) and ARG_TO_FUNCTION.get(arg):
            arg_method: Callable = ARG_TO_FUNCTION[arg]["function"]

            if ARG_TO_FUNCTION[arg]["pass_args"]:
                arg_method(args)
            else:
                arg_method()

    Timer().print_and_format_time("Total Time:")


if __name__ == "__main__":
    argument_parser(argv[1:])
