#############################################################
# FILE : stable_price.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: Check if price is stable over 3 years
#############################################################


def is_it_stable(value1, price1, price2, price3):
    """Return True if price remain stable during 3 years, else return False"""
    if abs(price1 - price2) < value1 and abs(price2 - price3) < value1:
        return True
    else:
        return False


