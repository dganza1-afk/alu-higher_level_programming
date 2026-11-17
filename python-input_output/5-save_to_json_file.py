#!/usr/bin/python3
"""Defines a function that saves an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write my_obj to filename using its JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
