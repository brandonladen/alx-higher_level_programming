#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = sorted(a_dictionary)
    for x in my_list:
        print("{}: {}".format(x, a_dictionary[x]))
