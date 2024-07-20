#!/usr/bin/python3
"""
This module contains a function that loads an object from a JSON file.
"""
import json
def load_from_json_file(filename):
    """
    Loads an object from a text file, using JSON representation.

    Args:
        filename (str): The name of the file.

    Returns:
        The object loaded from the file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
