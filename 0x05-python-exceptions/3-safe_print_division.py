#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        sur = a / b
    except ZeroDivisionError:
        sur = None
    finally:
        print("Inside result: {}".format(sur))
    return sur
