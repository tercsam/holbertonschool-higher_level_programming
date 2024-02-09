#!/usr/bin/python3
"define two intergers A and B"


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(a, (float, int)):
        raise TypeError("b must be an integer")

    return int(a + b)
