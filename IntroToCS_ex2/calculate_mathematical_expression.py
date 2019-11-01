#############################################################
# FILE : expression_,mathematical_calculate.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: calculate mathematical expressions.
#  from two numbers and char or string
#############################################################


def calculate_mathematical_expression(num1, num2, sgn):
    """Solve math equation and return the answer.
     if sgn is not arithmetic sign or the user try to divide in zero return none"""
    if num2 == 0:
        return None
    elif sgn == "+":
        return num1 + num2
    elif sgn == "-":
        return num2 - num1
    elif sgn == "/":
        return num1 / num2
    elif sgn == "*":
        return num1 * num2
    else:
        return None


def calculate_from_string(math_string):
    """Solve equation from string, using "calculate_mathematical_expression" function"""
    divided_str = math_string.split(" ")
    num1 = float(divided_str[0])
    num2 = float(divided_str[2])
    sgn = divided_str[1]
    if sgn == "+":
        return num1 + num2
    elif sgn == "-":
        return num1 - num2
    elif sgn == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return None
    elif sgn == "*":
        return num1 * num2
    else:
        return None
