#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    for i in my_string:
        if i != "c" or i != "C":
            result += i
            return result
