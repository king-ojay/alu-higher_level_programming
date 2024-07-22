#!/usr/bin/python3
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Name of the file to save the list
filename = "add_item.json"

# Initialize an empty list
my_list = []

# If the file exists, load its contents
if path.exists(filename):
    my_list = load_from_json_file(filename)

# Add all command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
