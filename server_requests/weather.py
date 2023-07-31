"""
file_name = weather.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/30/2023
Description: A file used to get weather data then format it
Edit Log: 
07/30/2023 
    - Moved over file from original tool receiver
    - Format string function for modularity
"""

from os import getenv

from requests import post
from stringcolor import cs as color

from utils.request_handshake import RequestHandshake
from utils.timer import Timer


def kelvin_to_fahrenheit(
    kelvin_degrees: float,
) -> float:
    """
    Convert temperature from Kelvin to Fahrenheit.

    Args:
        kelvin_degrees `float`: Temperature in Kelvin.

    Returns:
        `float`: Temperature in Fahrenheit.
    """

    return round(((kelvin_degrees - 273.15) * (9 / 5)) + 32, 2)


def format_and_print_weather_attributes(attribute: str, value: str, units="") -> None:
    """
    Format and print weather attributes.

    Args:
        attribute `str`: The attribute name.
        value `str`: The attribute value.
        units `str, optional`: The units for the attribute value. Defaults to an empty string.
    """

    attribute = color(attribute, "dodgerblue")
    value = color(value, "yellow")

    if units:
        value += f" {units}"
    print(f"{attribute:<40} {value:>30}")


@Timer(print_time=True, print_response=False)
@RequestHandshake()
def get_weather() -> None:
    """
    Retrieve the current weather information.

    This function makes an API request to get the current weather data and prints it to the console.

    Note:
        The `print_time` parameter of the `Timer` decorator is set to True,
        which prints the execution time of the function.
        The `print_response` parameter of the `Timer` decorator is set to False,
            which suppresses the printing of the function response.

    Raises:
        HTTPError: If there is an error occurred during the API request.
    """

    results = post(
        f"{getenv('TOOLS_URL')}/getCurrentWeather",
        json=RequestHandshake.base_request.copy(),
        timeout=5
    ).json()

    print(color("Current Weather", "grey4"))
    format_and_print_weather_attributes("Weather Type:", results["weather"][0]["main"])

    format_and_print_weather_attributes(
        "Weather Description:", results["weather"][0]["description"].title()
    )

    format_and_print_weather_attributes(
        "Feels Like:", kelvin_to_fahrenheit(results["main"]["feels_like"]), "°"
    )

    format_and_print_weather_attributes(
        "Temperature:", kelvin_to_fahrenheit(results["main"]["temp"]), "°"
    )

    format_and_print_weather_attributes(
        "Min Temperature:", kelvin_to_fahrenheit(results["main"]["temp_min"]), "°"
    )

    format_and_print_weather_attributes(
        "Max Temperature:", kelvin_to_fahrenheit(results["main"]["temp_max"]), "°"
    )

    if "wind" in results:
        format_and_print_weather_attributes(
            "Wind Speed:", results["wind"]["speed"], "m/s"
        )

    format_and_print_weather_attributes("Humidity:", results["main"]["humidity"], "%")

    if "clouds" in results:
        format_and_print_weather_attributes("Clouds:", results["clouds"]["all"], "%")

    if "rain" in results:
        format_and_print_weather_attributes(
            "Inches of Rain::", results["rain"]["1h"], "inches"
        )

    if "snow" in results:
        print(results["snow"])

    print()
