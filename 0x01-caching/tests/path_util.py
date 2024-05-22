#!/usr/bin/env python3
"""
Simple helper path utility module.
"""
import sys


def add_to_path():
    """Adds previous directory to path.
    """
    sys.path.append("../")


add_to_path()
