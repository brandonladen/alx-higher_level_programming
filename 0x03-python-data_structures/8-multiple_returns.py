#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    first = sentence[0]
    length = len(sentence)
    return length, first
