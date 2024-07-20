#!/usr/bin/python3
"""
This module contains a function that saves an object to a JSON file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a text file, using JSON representation.

    Args:
        my_obj (object): The object to be saved.
        filename (str): The name of the file.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

