#############################################################
# FILE : hello_turtle.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex1 2019
# DESCRIPTION: Include some math functions using "math" library
#############################################################


import math


def golden_ratio():
    """Print golden ratio"""
    print((1 + 5 ** 0.5) / 2)


def six_cubed():
    """Print 6 power 3"""
    print(math.pow(6, 3))


def hypotenuse():
    """Print the hypotenuse of straight angled triangle with 3 and 5 rib lengths"""
    print(math.sqrt(5*5 + 3*3))


def pi():
    """Print pi value"""
    print(math.pi)


def e():
    """Print e value"""
    print(math.e)


def triangular_area():
    _startNum = 1
    _endNum = 11
    _strResult = ''
    for i in range(_startNum, _endNum):
        _strResult = _strResult + str((i*i)/2) + ' '
    print(_strResult.strip())


if __name__ == "__main__":
    golden_ratio()
    six_cubed()
    hypotenuse()
    pi()
    e()
    triangular_area()

