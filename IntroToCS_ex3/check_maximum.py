#############################################################
# FILE : check_maximum.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex3 2019
# DESCRIPTION: Check maximum function with some inputs
#############################################################


from ex3.answer.ex3 import maximum


def test_maximum():
    test_lists = \
        [
            [1, 1, 1, 1, 1, 1, 1],
            [1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [1, 0, 1]
        ]
    test_result = True
    for i in range(len(test_lists)):
        if maximum(test_lists[i]) == max(test_lists[i]):
            print("Test " + str(i) + " passed")
        else:
            test_result = False
            print("Test " + str(i) + " failed")
    return test_result
