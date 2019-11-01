#############################################################
# FILE : largest_and_smallest.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: Return the max and min number of 3 inputs
#############################################################


def largest_and_smallest(num1, num2, num3):
    """Return the highest and smallest number between 3 numbers"""
    if num1 > num2:
        max_number = num1
        min_number = num2
    else:
        max_number = num2
        min_number = num1
    if num3 > max_number:
        return num3, min_number
    elif num3 < min_number:
        return max_number, num3
    else:
        return max_number, min_number

