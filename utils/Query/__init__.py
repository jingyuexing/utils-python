def Query(cls):
    """
    Decorator that modifies the __str__ method of a class to represent its instance variables
    in a query string format.

    Args:
    - cls: Class to be modified

    Returns:
    - Class: The modified class
    """
    def __str__(self):
        """
        Custom __str__ method that represents instance variables in a query string format.

        Returns:
        - str: Query string representation of the instance variables
        """
        cookies = []
        for key, value in self.__dict__.items():
            cookies.append(f"{key}={value}")
        return "&".join(cookies)
    cls.__str__ = __str__
    return cls