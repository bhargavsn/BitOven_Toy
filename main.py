#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# PYTHONSCRIPT:     main.py
# ------------------------------------------------------------------------------
__author__ = "Bhargav Srirangam"
# ------------------------------------------------------------------------------

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {__author__}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_word_with_stars(word):
    for letter in word:
        print("*" * len(letter), end=" ")
    print()

def print_megadeth_forever_pattern():
    pattern = [
        "******  *********   **       **   *********   **         **   ********** ",
        "**   **    **      ****     ****   **      **** **       **   **         ",
        "**    **   **     ** **   ** **   **     ** ** **     **    **         ",
        "**    **   **    **  ** **   **   **    **   ** **   **     **         ",
        "**   **    **   **    ***    **   **   **     ** ** **      *********  ",
        "******     **  **********    **   **  ********** **   **    **         ",
        "**         ** **        **   **   ** **        ** **     **  **         ",
        "**         ****          **  **   ****          ** **       ** **         ",
        "**         **              ** **     **          ** **        ** **       ",
        "**         **               ***       **         ** **         ** *********"
    ]

    for row in pattern:
        print(row)

# Call the function to print the pattern
print_megadeth_forever_pattern()


# Example usage:
#word = "example"
#print_word_with_stars(word)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   print_megadeth_forever_pattern()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
