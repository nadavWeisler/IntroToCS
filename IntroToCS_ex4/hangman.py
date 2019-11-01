#############################################################
# FILE : hangman.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex4 2019 - Hangman
# DESCRIPTION: Coding the game "hangman"
#############################################################


from hangman_helper import *
from string import ascii_lowercase


def update_word_pattern(word, pattern, letter):
    """Function that get word, pattern and letter and
    return a new pattern after reviling the given letter
    that missing in the given word"""
    new_string = ''
    for i in range(len(word)):
        if word[i] == letter:
            new_string += letter
        else:
            new_string += pattern[i]
    return new_string


def valid_input_letter(value):
    """Return true if the input letter is valid(alphabet and one letter) and false otherwise"""
    if type(value) == str and len(value) == 1 and value in ascii_lowercase:
        return True
    return False


def run_single_game(words_list):
    """Function that run single game of Hangman"""
    word = get_random_word(words_list)
    end_game = False
    errors = 0
    wrong_guess_lst = []
    already_chosen = []
    pattern = "_" * len(word)
    msg = DEFAULT_MSG
    while not end_game:
        display_state(pattern, errors, wrong_guess_lst, msg)
        user_input = get_input()

        if int(user_input[0]) == int(LETTER):
            if not valid_input_letter(user_input[1]):
                msg = NON_VALID_MSG
            elif user_input[1] in already_chosen:
                msg = ALREADY_CHOSEN_MSG + user_input[1]
            elif user_input[1] in word:
                pattern = update_word_pattern(word, pattern, user_input[1])
                msg = DEFAULT_MSG
            else:
                wrong_guess_lst.append(user_input[1])
                errors += 1
                msg = DEFAULT_MSG
            already_chosen.append(user_input[1])

        elif user_input[0] == HINT:
            msg = HINT_MSG + choose_letter(filter_words_list(words_list, pattern, wrong_guess_lst), pattern)

        if errors >= MAX_ERRORS or pattern.find("_") == -1:
            end_game = True

    if errors >= MAX_ERRORS:
        display_state(pattern, errors, wrong_guess_lst, LOSS_MSG + word, ask_play=True)
    else:
        display_state(pattern, errors, wrong_guess_lst, WIN_MSG, ask_play=True)


def letters_in_word(letters, word):
    """Function that get letters list and a word.
    Return True if the word contains one of them, False otherwise"""
    for letter in letters:
        if letter in word:
            return True
    return False


def word_and_pattern_fixed(word, pattern):
    """Get word and a pattern and return True if they are fixed (equal letters or '_')
    False otherwise"""
    for i in range(len(pattern)):
        if pattern[i] == "_":
            continue
        else:
            if pattern[i] != word[i]:
                return False
    return True


def filter_words_list(words, pattern, wrong_guess_lst):
    """Get words list pattern and list of wrong guesses,
     Return list of words that fit the pattern and wrong guesses"""
    result = []
    for word in words:
        if len(pattern) != len(word):
            continue
        elif letters_in_word(wrong_guess_lst, word):
            continue
        elif word_and_pattern_fixed(word, pattern):
            result.append(word)
    return result


def count_letter_in_words(words, letter):
    """Get words list and a letter
    Return count of the letter in all the words on the list"""
    count = 0
    for word in words:
        count += word.count(letter)
    return count


def choose_letter(words, pattern):
    """Get words list and a pattern.
    Return the most common letter in the list"""
    max_letter = ''
    max_count = 0
    for letter in ascii_lowercase:
        if letter in pattern:
            continue
        count = count_letter_in_words(words, letter)
        if count > max_count:
            max_count = count
            max_letter = letter
    return max_letter


def main():
    """Main function, play the game repeatedly until the user quit"""
    play = True
    word_list = load_words()
    while play:
        run_single_game(word_list)
        user_input = get_input()
        if not user_input[1]:
            play = False


if __name__ == "__main__":
    main()
