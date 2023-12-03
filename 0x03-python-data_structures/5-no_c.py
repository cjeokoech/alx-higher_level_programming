#!/usr/bin/env python3
def no_c(my_string):
    result = {ord(char): None for char in 'cC'}
    new = my_string.translate(result)
    return new
