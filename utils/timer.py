"""
file_name = timer.py
Creator: Ghazanfar Shahbaz
Last Updated: 07/29/2023
Description: A file used to time functions
Edit Log: 
07/29/2023 
    - Created timing decorator class logic
07/30/2023
    - Documented code
    - Added timing context manger logic
"""

from time import time

from stringcolor import cs as color


class Timer:
    """
    A decorator class for measuring the execution time of a function.
    """

    total_time: float = 0

    def __init__(self, print_time=False, print_response=False):
        """
        Initialize an instance of the Timer class.

        Args:
            print_time (bool, optional):
                Indicates whether to print the  execution time of the function.
                Defaults to False.
            print_response (bool, optional):
                Indicates whether to print the response of the function.
                Defaults to False.
        """

        self.start_time: float = time()
        self.print_time: bool = print_time
        self.print_response: bool = print_response

    def __enter__(self) -> "Timer":
        """Context manager enter method that returns the Timer instance.

        Returns:
            Timer: The Timer instance itself.
        """

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Context manager exit method to calculate and print the total execution time.

        Args:
            exc_type:
                The type of exception (if any) raised in the with block.
            exc_val:
                The exception value (if any) raised in the with block.
            exc_tb:
                The traceback object (if any) raised in the with block.
        """

        self.__time_function__()

    def __call__(self, func):
        """
        Callable method to decorate a function with execution time measurement.

        Args:
            func `callable`:
                The function to be decorated.

        Returns:
            `callable`:
                The decorated function.
        """

        def wrapper(*args, **kwargs):
            """
            Wrapper function that measures the execution time and calls the decorated function.

            Args:
                *args:
                    Variable length argument list.
                **kwargs:
                    Arbitrary keyword arguments.

            Returns:
                `any`:
                    The result of the decorated function call.
            """

            response: any = func(*args, **kwargs)

            if self.print_response:
                print(response)

            self.__time_function__()

            return response

        return wrapper

    def __time_function__(self) -> float:
        """
        Calculate and return the execution time of a function.

        Returns:
            `float` :
                The execution time in seconds.
        """

        execution_time = time() - self.start_time
        self.total_time += execution_time

        if self.print_time:
            print(f"Execution time: {color(execution_time, 'green')} seconds")
