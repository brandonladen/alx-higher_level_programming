#!/usr/bin/python3
"""
    Defines a function that prints a text with 2
    new lines after each of these characters: '.','?' and ':'
"""

def text_indentation(text):
    """
        Args:
            text: A parameter that passes in a text
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    modified_text = ""

    for word in text.split():
        modified_text += word
        if word[-1] in punctuation_marks:
            modified_text += '\n\n'
        else:
            modified_text += ' '

    print(modified_text.strip())
