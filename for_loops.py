"""
In this file, we will practice using for loops to access elements in arrays and strings.

Functions used:
range(start, stop, step=1) -> defines a range of values, not including the stop value
len(s) -> retrieves the length of a string

For loop syntax:
for _____ in _____:
    do something
"""
vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in range(0, 12, 2):
    print(val)

name = "Siddh Doshi"
for nam in range(-1, -11, -1):
    print(name[nam], end="")