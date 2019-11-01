import math
#############################################################
# FILE : shapes.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: Return circle, equilateral triangle and rectangle area
# ############################################################


def circle_area():
    """Return circle area when radius is given as input from user"""
    radius = float(input())
    return 2 * math.pi * radius


def rectangle_area():
    """Return square area when 2 ribs are given as user input"""
    first_rib = float(input())
    second_rib = float(input())
    return first_rib * second_rib


def equilateral_triangle_area():
    """Return equilateral triangle area when rib length is given as user input"""
    rib = int(input())
    return (math.sqrt(3) / 4) * (float(rib) ** 2)


def shape_area():
    """Return shape area depend on user choice, 1 circle, 2 rectangle, 3 equilateral triangle, else return None"""
    shape = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape == 1:
        return circle_area()
    elif shape == 2:
        return rectangle_area()
    elif shape == 3:
        return equilateral_triangle_area()
    else:
        return None

