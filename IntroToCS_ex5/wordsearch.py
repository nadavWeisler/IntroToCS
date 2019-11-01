#############################################################
# FILE : wordsearch.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex5 2019
# DESCRIPTION: Contains word search and all sub functions
#############################################################


import os
import sys


def read_file(filename, with_split=False):
    """Function that read files, with or without split
    :param filename path - string
    :param with_split - boolean
    :return return the file that was read"""
    result = []
    if not os.path.isfile(filename):
        print("File " + filename + " does not exist")
        return None

    with open(filename, "r") as f:
        lines = list(f.readlines())
        for line in lines:
            line = line.strip('\n')
            if with_split:
                result.append(line.split(","))
            else:
                result.append(line)
    return result


def read_matrix_file(filename):
    """Read matrix from file name using 'read_file'
    :param filename - string
    :return list of list"""
    return read_file(filename, True)


def read_wordlist_file(filename):
    """Read wordlist from file name using 'read_file'
    :param filename - string
    :return list of list"""
    return read_file(filename, False)


def check_direction(direction_string, valid_directions):
    """check direction string
    :param direction_string - string
    :param valid_directions - string
    :return boolean"""
    if direction_string is None or len(direction_string) == 0:
        return False
    for direction in direction_string:
        if direction not in valid_directions and len(direction) != 1:
            return False
    return True


def check_input_args(args, error_args_count="Some parameters are missing"):
    """Check input argument, need to be 5 of them, file name, w
    ord list, output and matrix files and direction
    :param args - list
    :return string or None"""
    if len(args) < 5:
        return error_args_count
    if not os.path.isfile(args[0]):
        return "Word list file: " + args[0] + " does not exist"
    elif not os.path.isfile(args[2]):
        return "Matrix file: " + args[2] + " does not exist"
    elif not check_direction(''.join(args[3:]), 'wxyzudlr'):
        return "One or more of the given directions are invalid"
    return None


def transpose_matrix(matrix):
    """Transpose matrix
    :param matrix - list of lists
    :return list of lists"""
    return map(list, zip(*matrix))


def exist_in_list(word_list, lst, from_begin):
    """Return dictionary of count of words from word_list on lst
    :param word_list - list of string
    :param lst - list of char
    :param from_begin - boolean
    :return dictionary"""
    result = {}
    if not from_begin:
        lst = lst[::-1]

    substring_strings = list(''.join(lst[i:j + 1]) for i in range(len(lst)) for j in range(i, len(lst)))

    for sub_str in substring_strings:
        if sub_str in word_list:
            if sub_str in result.keys():
                result[sub_str] += 1
            else:
                result[sub_str] = 1

    return result


def straight_search(word_list, matrix, up_or_down, from_begin):
    """Search words from word list on matrix
    :param word_list - list of strings
    :param matrix - list of lists
    :param up_or_down - boolean
    :param from_begin - boolean
    :return dictionary"""
    if up_or_down:
        matrix = transpose_matrix(matrix)
    result = {}
    for ln in matrix:
        result = merge_dictionaries(result, exist_in_list(word_list, ln, from_begin))
    return result


def get_diagonal_lines(matrix, up, right):
    """Get diagonal lines from matrix
    :param matrix - list of lists
    :param up - boolean
    :param right - boolean
    :return list of lists"""
    max_col = len(matrix[0])
    max_row = len(matrix)
    result = [[] for _ in range(max_row + max_col - 1)]
    get_columns_func(matrix, max_col, max_row, result, right, up)

    return result


def get_columns_func(matrix, max_col, max_row, result, right, up):
    for col in range(max_col):
        for row in range(max_row):
            if up:
                if right:
                    result[row + col].append(matrix[row][col])
                else:
                    result[row + col].append(matrix[row][max_col - col - 1])
            else:
                if right:
                    result[row + col].append(matrix[max_row - row - 1][col])
                else:
                    result[row + col].append(matrix[max_row - row - 1][max_col - col - 1])


def diagonal_search(word_list, matrix, up, right):
    """Search words from word list on matrix
        :param word_list - list of strings
        :param matrix - list of lists
        :param up - boolean
        :param right - boolean
        :return dictionary"""
    result = {}
    diagonals = get_diagonal_lines(matrix, up, right)
    for diagonal in diagonals:
        result = merge_dictionaries(result, exist_in_list(word_list, diagonal, True))

    return result


def search_up(word_list, matrix):
    """Search words from word_list in matrix, up direction
        :param word_list - list of strings
        :param matrix - list of lists
        :return list of lists"""
    return straight_search(word_list, matrix, True, False)


def search_down(word_list, matrix):
    """Search words from word_list in matrix, down direction
        :param word_list - list of strings
        :param matrix - list of lists
        :return list of lists"""
    return straight_search(word_list, matrix, True, True)


def search_right(word_list, matrix):
    """Search words from word_list in matrix, right direction
        :param word_list - list of strings
        :param matrix - list of lists
        :return list of lists"""
    return straight_search(word_list, matrix, False, True)


def search_left(word_list, matrix):
    """Search words from word_list in matrix, left direction
        :param word_list - list of strings
        :param matrix - list of lists
        :return list of lists"""
    return straight_search(word_list, matrix, False, False)


def search_up_left(word_list, matrix):
    """Search words from word_list in matrix, up left direction
        :param word_list - list of strings
        :param matrix - list of lists
        :return list of lists"""
    return diagonal_search(word_list, matrix, True, False)


def search_up_right(word_list, matrix):
    """Search words from word_list in matrix, up right direction
        :param word_list - list of strings
        :param matrix - list of lists
        :return list of lists"""
    return diagonal_search(word_list, matrix, True, True)


def search_down_left(word_list, matrix):
    """Search words from word_list in matrix, down left direction
    :param word_list - list of strings
    :param matrix - list of lists
    :return list of lists"""
    return diagonal_search(word_list, matrix, False, False)


def search_down_right(word_list, matrix):
    """Search words from word_list in matrix, down right direction
    :param word_list - list of strings
    :param matrix - list of lists
    :return list of lists"""
    return diagonal_search(word_list, matrix, False, True)


def merge_dictionaries(dic1, dic2):
    """Merge two dictionaries
    :param dic1 - dictionary
    :param dic2 - dictionary
    :return dictionary"""
    result = dic1.copy()
    for key in dic2:
        if key in dic1.keys():
            result[key] += dic2[key]
        else:
            result[key] = dic2[key]
    return result


def find_words_in_matrix(word_list, matrix, direction):
    """Find words from word list on matrix by direction
    :param word_list - list of string
    :param matrix - list of lists
    :param direction - list of strings
    :return list of tuples"""
    result_dictionary = {}
    direction_lst = list(direction)
    for i in range(len(direction_lst)):
        if direction[i] in direction_lst[:i]:
            continue
        if direction[i] == 'u':
            result_dictionary = merge_dictionaries(result_dictionary, search_up(word_list, matrix))
        elif direction[i] == 'd':
            result_dictionary = merge_dictionaries(result_dictionary, search_down(word_list, matrix))
        elif direction[i] == 'r':
            result_dictionary = merge_dictionaries(result_dictionary, search_right(word_list, matrix))
        elif direction[i] == 'l':
            result_dictionary = merge_dictionaries(result_dictionary, search_left(word_list, matrix))
        elif direction[i] == 'w':
            result_dictionary = merge_dictionaries(result_dictionary, search_up_right(word_list, matrix))
        elif direction[i] == 'x':
            result_dictionary = merge_dictionaries(result_dictionary, search_up_left(word_list, matrix))
        elif direction[i] == 'y':
            result_dictionary = merge_dictionaries(result_dictionary, search_down_right(word_list, matrix))
        elif direction[i] == 'z':
            result_dictionary = merge_dictionaries(result_dictionary, search_down_left(word_list, matrix))

    result = []
    for key in result_dictionary:
        result.append((key, result_dictionary[key]))
    return result


def write_output_file(results, output_filename):
    """Write output file
    :param results - list of tuples
    :param output_filename - string"""
    if os.path.isfile(output_filename):
        os.remove(output_filename)

    with open(output_filename, 'w') as f:
        for item in results:
            f.write(item[0] + "," + str(item[1]) + '\n')


def main():
    """Main program function"""
    args = sys.argv[1:]
    check_args = check_input_args(args)
    if check_args is not None:
        print(check_args)
    else:
        write_output_file(
            results=find_words_in_matrix(
                word_list=read_wordlist_file(filename=args[0]),
                matrix=read_matrix_file(filename=args[2]),
                direction=list(''.join(args[3:]))),
            output_filename=args[1])


if __name__ == '__main__':
    main()
