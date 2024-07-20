#!/usr/bin/python3
"""
This module adds all arguments to a Python list and saves them to a file.

The list is saved as a JSON representation in a file named add_item.json.
"""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def main():
    """
    Main function to add all command line arguments to a list and save to a file.
    """
    filename = 'add_item.json'

    # Load existing data from the file, if it exists
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add new items from command line arguments
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)

if __name__ == '__main__':
    main()
