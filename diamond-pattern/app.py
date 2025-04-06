import streamlit as st

# Diamond pattern using loops and string repetition

# Define the size of the diamond (number of rows in the upper half)
n = 5

# Upper half of the diamond (including the middle line)
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * (2 * i - 1))

# Lower half of the diamond (inverted pyramid)
for i in range(n - 1, 0, -1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * (2 * i - 1))