#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
    """classMyList"""
    def print_sorted(self):
        """Print sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
