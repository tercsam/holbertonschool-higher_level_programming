#!/usr/bin/python3
"define a class with a private instance attribut 'size'"


class Square:
    "Square class with a private instance attribut"
    def __init__(self, size):
        "initalize square using pirvate attribute size as args"
        self.__size = size
