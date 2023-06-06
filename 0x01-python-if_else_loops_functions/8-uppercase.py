#!/usr/bin/python3
def uppercase(str):
    string = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            string = string + chr((ord(char) - 32))
        else:
            string += char
    print(f"{string}")
