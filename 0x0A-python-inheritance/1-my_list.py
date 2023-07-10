#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):

    def print_sorted(self):
        """
        Args:
            my_list: list to sort in ascending order
        """
        print(sorted(self))
