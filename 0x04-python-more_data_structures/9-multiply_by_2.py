#!/usr/bin/python3

# 9-multiply_by_2.py


def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2"""
    new_dic = {}
    for i in a_dictionary:
        new_dic[i] = a_dictionary[i] * 2
    return new_dic
