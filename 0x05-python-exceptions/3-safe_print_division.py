#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = int(a / b)
    except (ZeroDivisionError,TypeError):
        div = (None)
    finally:
        print("Inside results: {:d}".format(div))
        return(div)
