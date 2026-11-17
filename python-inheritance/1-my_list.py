#!/usr/bin/python3
"""Defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list with a print_sorted method."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
