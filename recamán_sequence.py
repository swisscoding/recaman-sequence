#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Find Recamán's index of number | ----\n", fg("red")))

# user interaction
number = int(input("Enter positive integer: "))

# sequence
sequence = [0]

# function
def recaman_index(integer):
    subtraction = sequence[-1] - len(sequence)

    if subtraction > 0 and not subtraction in sequence:
        sequence.append(subtraction)
    else:
        sum = sequence[-1] + len(sequence)
        sequence.append(sum)

    if sequence[-1] == integer:
        return sequence.index(integer)
    else:
        return recaman_index(number)

# output
result = stylize(recaman_index(number), fg("red"))
print(f"\nRecamán's sequence:\n{sequence}")
print(f"\nRecamán's index of {number} is: {result}.\n")
