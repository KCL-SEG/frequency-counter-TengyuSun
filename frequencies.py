"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for key in items:
        frequencies[key] = frequencies.get(key, 0) + 1
    return frequencies
