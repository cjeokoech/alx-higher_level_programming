#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    pre = 0
    for x in roman_string:
        value = nums[x]
        if value < pre:
            result -= value
        else:
            result += value
            pre = value
            return result
