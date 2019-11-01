#############################################################
# FILE : wordsearch.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex5 list and files 2019
# DESCRIPTION: Contains tests for merge_directories
#############################################################

from wordsearch import merge_dictionaries


def test_merge_dictionaries():
    dic1 = [
        {},
        {},
        {'hello': 1},
        {'hello': 1},
        {'hello': 1, 'chair': 1}
    ]
    dic2 = [
        {},
        {'hello': 1},
        {},
        {'chair': 1},
        {'hello': 1}
    ]
    dic_merge = [
        {},
        {'hello': 1},
        {'hello': 1},
        {'hello': 1, 'chair': 1},
        {'hello': 2, 'chair': 1}
    ]

    for i in range(len(dic_merge)):
        if merge_dictionaries(dic1[i], dic2[i]) != dic_merge[i]:
            print("Test fail")
            return False
    print("Test succeeded!")
    return True


if __name__ == '__main__':
    test_merge_dictionaries()
