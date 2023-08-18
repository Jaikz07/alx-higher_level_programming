#!/usr/bin/python3

# 7-update_dictionary.py


def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary."""
    n_dic = {key: value}
    a_dictionary.update(n_dic)
    return a_dictionary
