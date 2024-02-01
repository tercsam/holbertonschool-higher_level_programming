#!/usr/bin/python3

def no_c(my_string):
    noCstring = str.maketrans(", ", "cC")
    return my_string.translate(noCstring)
