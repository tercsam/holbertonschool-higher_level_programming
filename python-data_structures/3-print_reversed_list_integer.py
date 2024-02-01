#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for int in reversed(my_list):
        print(str.format('{:d}', int))
