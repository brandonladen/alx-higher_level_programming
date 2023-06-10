#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(tuple_a) == 0:
        list_a[0] = 0
        list_a[1] = 0
    elif len(tuple_a) == 1:
        list_a[1] = 0
    elif len(tuple_b) == 0:
        list_b[0] = 0
        list_b[1] = 0
    elif len(tuple_b) == 1:
        list_b[1] = 0

    new_list = list_a + list_b
    new_list1 = new_list[0] + new_list[2]
    new_list2 = new_list[1] + new_list[3]
    final_list = new_list1 + new_list2
    my_tuple = tuple(final_list)
    return my_tuple
