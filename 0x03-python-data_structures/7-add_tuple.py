#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_a) != 0:
        list_a = list(tuple_a)
        list_a.append(0)
        tuple_a = tuple(list_a)
    elif len(tuple_a) == 0:
        list_a = list(tuple_a)
        list_a.append(0)
        list_a.append(0)
        tuple_a = tuple(list_a)
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[:2]

    if len(tuple_b) < 2 and len(tuple_b) != 0:
        list_a = list(tuple_b)
        list_a.append(0)
        tuple_b = tuple(list_a)
    elif len(tuple_b) == 0:
        list_a = list(tuple_b)
        list_a.append(0)
        list_a.append(0)
        tuple_b = tuple(list_a)
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]

    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
