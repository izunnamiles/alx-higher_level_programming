#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divide = a / b
    except (TypeError, ZeroDivisionError):
        divide = None
    finally:
        print("Inside result: {}".format(divide))
    return (divide)
