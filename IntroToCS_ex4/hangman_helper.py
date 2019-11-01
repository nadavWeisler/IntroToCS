import random

MAX_ERRORS = 6
START_MSG = "Let's begin!"
WIN_MSG = 'Correct guess, this is the word!!!'
LOSS_MSG = 'You have run out of guesses, the word was: '
ALREADY_CHOSEN_MSG = 'You have already chosen '
NON_VALID_MSG = 'Please enter a valid letter'
HINT_MSG = 'Consider choosing: '
NO_HINTS_MSG = 'Hints not supported'
DEFAULT_MSG = ''
MSG_WIN_COLOR = "green"
MSG_WARN_COLOR = "red"
MSG_HINT_COLOR = "blue"
HINT = 1
LETTER = 2
PLAY_AGAIN = 3
INIT_ALPHA_ORDER = 97

_rand = random.Random()
play_again_request = False


def seed(a=None):
    _rand.seed(a)


def load_words(file='words.txt'):
    '''Loads a list of 58110 words from words.txt file'''
    words = []
    f_words = open(file)
    for line in f_words:
        word = line.strip()
        if (word.isalpha()):
            words.append(line.strip())
    f_words.close()
    return words


def get_random_word(words_list):
    '''
    Gets a random word out of the given list of words
    '''
    return _rand.choice(words_list)


def get_input():
    choice = input()
    if play_again_request:
        return PLAY_AGAIN, not (choice and choice[0] in 'nN')
    elif not choice:
        return HINT, None
    else:
        return LETTER, choice


def display_state(pattern, error_count, wrong_guess_lst, msg, ask_play=False):
    global play_again_request
    play_again_request = ask_play
    print('Number of errors:', error_count)
    print('Wrong guesses:', wrong_guess_lst)
    print('Current pattern:', pattern)
    print(msg)
    if msg:
        print()
    if ask_play:
        print('Play again? (Y/N) ', end='')
    else:
        print('Guess letter: (No input to request hint.) ', end=' ')