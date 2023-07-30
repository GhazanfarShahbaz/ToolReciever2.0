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
"""

from argparse import ArgumentParser, Namespace
from typing import Dict, Callable

from server_requests.weather import get_weather
from utils.timer import Timer

PARSER: ArgumentParser = ArgumentParser()

# ARGUMENTS
PARSER.add_argument("-w", "--weather", help="Get todays weather", action="store_true")

ARG_TO_FUNCTION: Dict[str, Callable] = {
    "weather": get_weather,
}

if __name__ == "__main__":
    args: Namespace = PARSER.parse_args()

    for arg in vars(args):
        if getattr(args, arg) and ARG_TO_FUNCTION.get(arg):
            ARG_TO_FUNCTION[arg]()

    Timer().print_and_format_time("Total Time:")
