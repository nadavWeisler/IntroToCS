#############################################################
# FILE : largest_and_smallest.py
# WRITER : Nadav Weisler , Weisler , 316493758
# EXERCISE : intro2cs ex2 2019
# DESCRIPTION: test largest_and_smallest function from
#           largest_and_smallest.py
#############################################################


from exp.ex2.largest_and_smallest import largest_and_smallest


def test_largest_and_smallest():
    """Test largest_and_smallest function, return True if succeeded and False otherwise"""
    if ((((largest_and_smallest(1, 1, 1) != (1, 1) or largest_and_smallest(1, 2, 3) != (3, 1)) or
        largest_and_smallest(1, 2, 2) != (2, 1)) or largest_and_smallest(1, 1, 2) != (2, 1)) or
            largest_and_smallest(3, 2, 4) != (4, 2)):
        print("test fail")
        return False
    else:
        print("Test for largest_and_smallest succeeded!")
        return True


if __name__ == '__main__':
    test_largest_and_smallest()
