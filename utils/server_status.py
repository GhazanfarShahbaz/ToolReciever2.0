"""
file_name = server_status.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/29/2023
Description: A file used to check the server status
Edit Log: 
07/29/2023 
    - Moved over file from original tool receiver
"""

import os
import requests


def server_status() -> bool:
    """
    Check if the server is running correctly, by pinging it

    Returns:
        `bool``: Returns true if server is running, false if not
    """

    url: str = os.getenv("BASE_URL")
    header: requests.Response = requests.head(url=url, timeout=5)

    return header.status_code == 200
