#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raise an Exception: area is not implemented."""
        raise Exception("area() is not implemented")
