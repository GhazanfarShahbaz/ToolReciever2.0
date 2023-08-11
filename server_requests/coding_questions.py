"""
file_name = events.py
Creator: Ghazanfar Shahbaz
Last Updated: 08/05/2023
Description: A file used to get random coding question
Edit Log: 
08/05/2023 
- Created new file
08/10/2023
- Documented functions
"""

from argparse import Namespace
from os import getenv

from requests import get, post
from stringcolor import cs as color

from utils.timer import Timer


def setup_random_leetcode_question_request(args: Namespace) -> dict:
    """
    Set up a random LeetCode question request based on the provided arguments.

    Args:
        args (Namespace): The parsed command-line arguments.

    Returns:
        dict: A dictionary representing the filter form for the LeetCode question request.
    """

    return {
        "filterForm": {
            "difficulty": args.lc_difficulty.title() if args.lc_difficulty else None,
            "tag": args.lc_tag if args.lc_tag else None,
            "subscription": False,
        }
    }


def setup_random_codechef_question_request(args: Namespace) -> dict:
    """
    Set up a random CodeChef question request based on the provided arguments.

    Args:
        args (Namespace): The parsed command-line arguments.

    Returns:
        dict: A dictionary representing the filter form for the CodeChef question request.
    """

    return {
        "filterForm": {
            "difficulty": args.cf_difficulty.lower() if args.cf_difficulty else None,
        }
    }


def print_question_link(base_string: str, link: str) -> None:
    """
    Print the question link with colored formatting.

    Args:
        base_string (str): The base string to be displayed.
        link (str): The link to be displayed.

    Returns:
        None
    """

    print(f"{color(base_string, 'dodgerblue')} {color(link, 'yellow')}")


@Timer(print_time=True, print_response=False)
def get_random_leetcode_question(args: Namespace) -> None:
    """
    Get a random LeetCode question and print the question link.

    Args:
        args (Namespace): The parsed command-line arguments.

    Returns:
        None
    """

    request = setup_random_leetcode_question_request(args)

    results = post(
        url=f"{getenv('BASE_URL')}/coding_questions/getRandomLeetcodeProblem",
        json=request,
        timeout=5,
    ).json()

    print_question_link("Leetcode Question Link:", results["link"])


@Timer(print_time=True, print_response=False)
def get_random_codechef_question(args: Namespace) -> None:
    """
    Get a random CodeChef question and print the question link.

    Args:
        args (Namespace): The parsed command-line arguments.

    Returns:
        None
    """

    request = setup_random_codechef_question_request(args)

    results = post(
        url=f"{getenv('BASE_URL')}/coding_questions/getRandomCodeChefProblem",
        json=request,
        timeout=5,
    ).json()

    print_question_link("Codechef Question Link:", results["link"])


@Timer(print_time=True, print_response=False)
def get_random_euler_question() -> None:
    """
    Get a random Euler question and print the question link.

    Returns:
        None
    """

    results = get(
        url=f"{getenv('BASE_URL')}/coding_questions/getRandomEulerProblem", timeout=5
    ).json()

    print_question_link("Euler Question Link:", results["link"])
