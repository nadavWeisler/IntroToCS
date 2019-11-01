#############################################################
# FILE : check_update_word_pattern.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex4 2019 - Hangman
# DESCRIPTION: test several inputs for the
#     function "update_word_pattern from hangman.py
#############################################################


from hangman import update_word_pattern


def test_update_word_pattern():
    """Function that test several inputs for the
    function "update_word_pattern from hangman.py"""
    words = [
        'hello',
        'hello',
        'hello',
        'hello'
    ]
    patterns = [
        '_____',
        'hell_',
        'hell_',
        'h____'

    ]
    letters = [
        'h',
        'h',
        'o',
        'd'
    ]
    results = [
        "h____",
        "hell_",
        "hello",
        "h____"
    ]
    for i in range(len(words)):
        if update_word_pattern(words[i], patterns[i], letters[i]) != results[i]:
            print("Test failed")
            return False
    print("Test done!")
    return True


if __name__ == '__main__':
    test_update_word_pattern()