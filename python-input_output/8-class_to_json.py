#!/usr/bin/python3
"""Defines a function that returns an object's attributes as a dict."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization."""
    return obj.__dict__
