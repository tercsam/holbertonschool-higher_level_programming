#!/usr/bin/python3
"define a class with a private instance attribut 'size'"


class Square:
    "Square class with a private instance attribut"
    def __init__(self, size):
        "initalize square using pirvate attribute size as args"
        self.__size = size


def __init__(self, size=0):
    if isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


def area(self):
    return self.__size**2

    pass
