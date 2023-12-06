#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for value in a_dictionary:
        a_dictionary[value] *= 2
        return a_dictionary
#    new = [value * 2 for value in a_dictionary]
 #   print("{}: {}".format(value, a_dictionary[value])
