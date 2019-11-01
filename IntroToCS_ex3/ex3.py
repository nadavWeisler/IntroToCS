#############################################################
# FILE : ex3.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex3 2019
# DESCRIPTION: Ex3 exercise, contain 9 functions:
#   input_list, concat_list, maximum, cyclic,
#   seven_boom, histogram, prime_factors,
#   cartesian, pairs
#############################################################


def input_list():
    """Function that return a list of user inputs"""
    return_list = []
    input_string = input()
    while input_string != '':
        return_list.append(input_string)
        input_string = input()
    return return_list


def concat_list(str_list):
    """Return concat string of string list"""
    return_string = ''
    start = True
    for str_value in str_list:
        if not start:
            return_string + " "
        else:
            start = False
        return_string += str_value
    return return_string


def maximum(num_list):
    """Return the maximum number between number list"""
    return_value = None
    for num in num_list:
        if return_value is None or num > return_value:
            return_value = num
    return return_value


def cyclic(lst1, lst2):
    """Return the cyclic of 2 lists"""
    if len(lst1) != len(lst2):
        return False
    lst2_first_in_lst1 = []
    for i in range(len(lst1)):
        if lst1[i] not in lst2:
            return False
        if lst1[i] == lst2[0]:
            lst2_first_in_lst1.append(i)

    if_cyclic = True
    for count_item in lst2_first_in_lst1:
        for i1 in range(len(lst1)):
            if lst1[i1] != lst2[(i1 + count_item) % len(lst1)]:
                if_cyclic = False
        if if_cyclic:
            return True
        else:
            if_cyclic = True
    return False


def seven_boom(num):
    """Return list of 7 boom game of input number"""
    lst = []
    for i in range(num):
        if i + 1 % 7 == 0:
            lst.append('boom')
        else:
            lst.append(str(i + 1))
    return lst


def histogram(n, num_list):
    """Return histograms of number and list"""
    lst = []
    for i in range(n):
        count = 0
        for num in num_list:
            if num == i:
                count += 1
        lst.append(count)
    return lst


def prime_factors(num):
    """Return prime factors on input number"""
    index = 2
    return_factors = []
    while index ** 2 <= num:
        if num % index:
            index += 1
        else:
            num = num / index
            return_factors.append(index)
    if num > 1:
        return_factors.append(num)
    return return_factors


def cartesian(lst1, lst2):
    """Return cartesian of 2 lists"""
    lst = []
    for item1 in lst1:
        for item2 in lst2:
            lst.append([item1, item2])
    return lst


def pairs(num_list, num):
    """Return all the pairs from list of numbers that together equal num"""
    ret = []
    for num1 in num_list:
        for num2 in num_list:
            if num1 + num2 == num:
                if ([num1, num2] not in ret) and ([num2, num1] not in ret):
                    ret.append([num1, num2])
    return ret
