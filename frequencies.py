"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for key in items:
        frequencies[str(key)] = frequencies.get(str(key), 0) + 1
    return frequencies

demo = [1,22,22,33,33,1,'1']
print(frequencies(demo))