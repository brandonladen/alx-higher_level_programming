#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 1
    try:
        for elem in range(x):
            counter += 1
            print("{}".format(my_list[elem]), end="")

        print()
        return (x)
    except IndexError:
        x = x - counter
        for elem in range(x):
            print("{}".format(my_list[elem]), end="")

        print()
        return (elem)
