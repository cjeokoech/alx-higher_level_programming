#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
    """classMyList"""
    def print_sorted(self):
        """Print sorted list"""
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
