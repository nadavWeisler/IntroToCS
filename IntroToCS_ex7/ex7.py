#############################################################
# FILE : ex7.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex7
# DESCRIPTION: Contains recursive functions
#############################################################


def print_to_n(n):
    """
    Print number from 1 to n
    :param n:number
    :return:
    """
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)


def print_reversed(n):
    """
    Print number from n to 1
    :param n: number
    :return:
    """
    if n < 1:
        return
    print(n)
    print_reversed(n - 1)


def has_divider_smaller_than(n, i):
    """
    Get True if n has a divided smaller than i
    :param n: number
    :param i: number
    :return: boolean
    """
    print(n, i)
    if i <= 1:
        return False
    else:
        if n % i == 0:
            return True
        else:
            return has_divider_smaller_than(n, i - 1)


def is_prime(n):
    """
    Return if n is prime
    :param n: number
    :return: boolean
    """
    return not has_divider_smaller_than(n, int(n / 2))


def get_factorial(n):
    """
    Get factorial of n
    :param n: number
    :return: number
    """
    if (n <= 1):
        return n
    else:
        return n * (get_factorial(n - 1))


def exp_n_x(n, x):
    """
    Get exp
    :param n:
    :param x:
    :return:
    """
    if (n <= 1):
        return x
    else:
        return exp_n_x(n - 1, x) + (x ** n / get_factorial(n))


def play_hanoi(hanoi, n, src, dest, temp):
    """
    Function with the algorithm for hanoi game
    :param hanoi: hanoi game object
    :param n: src tower disk count
    :param src: src tower count
    :param dest: dest tower count
    :param temp: temp tower count
    """
    if n == 1:
        hanoi.move(src, dest)
        return
    play_hanoi(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n - 1, temp, dest, src)


def permutations(head, tail='', printed=[]):
    """
    Print permutations of string
    """
    if len(head) == 0 and tail not in printed:
        print(tail)
        printed.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i + 1:], tail + head[i], printed)


def print_sequences(char_list, n, ret=[]):
    """
    Print all sequences of char list with n length
    :param char_list:list
    :param n:number
    :param ret:list
    """
    if (len(ret) == n):
        print("".join(ret))
    else:
        for item in char_list:
            new_list = ret[:]
            new_list.append(item)
            print_sequences(char_list, n, new_list)


def print_no_repetition_sequences(char_list, n):
    """
    Return char list sequences without repetition
    :param char_list:list
    :param n:number
    :param printed:list
    """
    for i in range(len(char_list)):
        if (len(char_list) == n):
            permutations("".join(char_list))
        else:
            new_list = char_list[:]
            new_list.pop(i)
            print_no_repetition_sequences(new_list, n)


def parentheses(n, count_open=0, count_close=0, item_str="", ret=[]):
    """
    Return all parentheses with n length
    :param n: number
    :param count_open: number
    :param count_close: number
    :param item_str: string
    :param ret: list
    :return:
    """
    if count_close == int(n):
        ret.append(item_str)
    else:
        if count_open == int(n):
            parentheses(n, count_open, count_close + 1, item_str + ")")
        else:
            if count_open == count_close:
                parentheses(n, count_open + 1, count_close, item_str + "(")
            else:
                parentheses(n, count_open + 1, count_close, item_str + "(")
                parentheses(n, count_open, count_close + 1, item_str + ")")
    return ret


def up_and_right(n, k, current=(0, 0), ret=''):
    """
    Print all the routes from n to k
    :param n:number
    :param k:number
    :param current:tuple
    :param ret:string
    """
    if current == (n, k):
        print(ret)
    if current[0] <= n:
        up_and_right(n, k, (current[0] + 1, current[1]), ret + "r")
    if current[1] <= k:
        up_and_right(n, k, (current[0], current[1] + 1), ret + "u")


def flood_fill(image, start):
    """
    Update image by flood fill algorithm
    :param image: matrix
    :param start: start point (tuple)
    """
    image[start[0]][start[1]] = '*'
    if start[0] > 0 and image[start[0] - 1][start[1]] == '.':
        flood_fill(image, (start[0] - 1, start[1]))
    if start[0] < (len(image) - 1) and image[start[0] + 1][start[1]] == '.':
        flood_fill(image, (start[0] + 1, start[1]))
    if start[1] > 0 and image[start[0]][start[1] - 1] == '.':
        flood_fill(image, (start[0], start[1] - 1))
    if start[1] < len(image[0]) - 1 and image[start[0]][start[1] + 1] == '.':
        flood_fill(image, (start[0], start[1] + 1))


if __name__ == '__main__':
    print_no_repetition_sequences(['a', 'b'], 2)