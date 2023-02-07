#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, 'w') as f:
        return json.loads(f)
