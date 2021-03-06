"""

Miscellaneous functions for working with files

"""

import os

import csv
import json


def canonicalize_path(path: str):
    """Converts a path string to its canonical form (easier for comparisons)"""
    return os.path.abspath(os.path.realpath(os.path.expanduser(path)))

