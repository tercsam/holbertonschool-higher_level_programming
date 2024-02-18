#!/usr/bin/python3
"""Check if it's exactly the same"""


def is_kind_of_class(obj, a_class):
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    return False
