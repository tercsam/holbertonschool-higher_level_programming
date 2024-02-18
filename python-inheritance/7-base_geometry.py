#!/usr/bin/python3
""" 1-create an empty class
    2-add a public instance method
    3-add another public method
"""


class BaseGeometry:
    """ 1-empty class
        2-raise an Exception:
        3-add def integer_validator(self, name, value):
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
