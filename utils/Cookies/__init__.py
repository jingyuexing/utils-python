from pydantic import dataclasses
from dataclasses import dataclass


def Cookies(cls):
    """
    Decorator that modifies the __str__ method of a class to represent its instance variables
    in a format similar to cookies.

    Args:
    - cls: Class to be modified

    Returns:
    - Class: The modified class
    """

    def __str__(self):
        """
        Custom __str__ method that represents instance variables in a format similar to cookies.

        Returns:
        - str: String representation of the instance variables in cookie-like format
        """
        cookies = []
        for key, value in self.__dict__.items():
            cookies.append(f"{key}={value}")
        return ";".join(cookies)

    cls.__str__ = __str__
    return cls
