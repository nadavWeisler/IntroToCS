#############################################################
# FILE : quadratic_equation.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: esulva quadratic equation
#############################################################


import math


def quadratic_equation(num1, num2, num3):
    """Solve quadratic equation"""
    delta = (num2 ** 2) - (4 * num1 * num3)
    if delta < 0:
        return None
    elif delta > 0:
        return (-num2 + math.sqrt(delta)) / 2 * num1, (-num2 - math.sqrt(delta)) / 2 * num1
    else:
        return -num2 / 2 * num1, None


def quadratic_equation_user_input():
    """Solve quadratic equation from user input using "quadratic_equation" function"""
    nums_string = input("Insert coefficients a, b, and c: ")
    nums_split = nums_string.split(" ")
    sols = quadratic_equation(float(nums_split[0]), float(nums_split[1]), float(nums_split[2]))
    if sols is None:
        print("The equation has no solutions")
    elif sols[1] is None:
        print("The equation has 1 solution: " + str(sols[0]))
    else:
        print("The equation has 2 solutions: " + str(sols[0]) + " and " + str(sols[1]))


