#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    first = sentence[0]
    length = len(sentence)
    return length, first
