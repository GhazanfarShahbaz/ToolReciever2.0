"""
file_name = logs.py
Creator: Ghazanfar Shahbaz
Last Updated: 08/04/2023
Description: A file used to get  server logs
Edit Log: 
07/30/2023 
    - Moved over logic from original tool receiver
"""

from datetime import datetime
from typing import List
from os import getenv

from requests import post

from utils.request_handshake import RequestHandshake
from utils.timer import Timer


def write_log_file(file_name: str, logs: List[str]) -> None:
    """
    Write the logs to a file for the app.

    Args:
        file_name `str`: The name of the file.
        logs `List[str]`: The logs to write to the file.
    """

    with open(f"{getenv('LOG_PATH')}/{file_name}", "w", encoding="UTF-8") as log_file:
        for line in logs:
            log_file.write(line)


@Timer(print_time=True, print_response=False)
@RequestHandshake()
def get_logs() -> None:
    """
    Retrieve and saves today's logs.

    Note:
        The `print_time` parameter of the `Timer` decorator is set to True,
        which prints the execution time of the function.
        The `print_response` parameter of the `Timer` decorator is set to False,
            which suppresses the printing of the function response.

    Raises:
        HTTPError: If there is an error occurred during the API request.
    """

    base_request: dict = RequestHandshake.base_request.copy()
    results = post(
        url=f"{getenv('TOOLS_URL')}/getLogs", json=base_request, timeout=5
    ).json()

    current_date: str = datetime.now().strftime("%Y-%m-%d")

    for app_name, logs in results.items():
        file_name: str = f"{app_name}_{current_date}.log"

        write_log_file(file_name, logs)
