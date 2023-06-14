#!/usr/bin/python3
def best_score(a_dictionary):
    H_score = 0
    name = ""
    if a_dictionary == None:
        return None
    for k, v in a_dictionary.items():
        if v > H_score:
            H_score = v
            name = k
    return name
