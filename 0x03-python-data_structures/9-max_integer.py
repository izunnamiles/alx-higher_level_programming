#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 0:
        return "None"
    if isinstance(my_list, list):
        my_list.sort()
        return (my_list[-1])
