import math
import sys
import wave_helper
import os

MusicalNoteFreq = {
    "A": 440,
    "B": 494,
    "C": 523,
    "D": 587,
    "E": 659,
    "F": 698,
    "G": 784,
    "Q": 0
}

MAX_INT = 32767
MIN_INT = -32768
FRAME_RATE = 2000


def reverse_wave(lst):
    """
    Reverse list of lists
    :param lst: list of lists
    :return: reversed list
    """
    return lst[::-1]


def speed_wave(lst):
    """
    Delete even indexes of list
    :param lst: list of list
    :return: list of odd indexes of the original list
    """
    return lst[0::2]


def slow_wave(lst):
    """
    Between each item, add the average of its neighbors
    :param lst: list of list
    :return: new list
    """
    result = []
    for item in range((len(lst) - 1)):
        result.append(lst[item])
        result.append(get_average_item(item, lst))
    result.append(lst[-1])
    return result


def get_average_item(index, lst, take_back=False):
    """
    this function calculates the average of the element in a list, and his
    sequential indexes
    :param index: the index
    :param lst: list of elements
    :return: the average of the needed elements
    """
    if take_back:
        return [
            int((lst[index - 1][0] + lst[index][0] + lst[index + 1][
                0]) / 3),
            int((lst[index - 1][1] + lst[index][1] + lst[index + 1][
                1]) / 3)
        ]

    return [
        int((lst[index][0] + lst[index + 1][0]) / 2),
        int((lst[index][1] + lst[index + 1][1]) / 2)
    ]


def increase_wave(lst):
    """
    multiply the elements of the list, in order to increase the volume
    :param lst: list of lists
    :return: updated list
    """
    result = []
    for item in lst:
        result.append(
            [
                int(max(min(item[0] * 1.2, MAX_INT), MIN_INT)),
                int(max(min(item[1] * 1.2, MAX_INT), MIN_INT))
            ]
        )
    return result


def decrease_wave(lst):
    """
    divides the elements of the list, in order to decrease the volume
    :param lst: list of lists
    :return: updated list
    """
    result = []
    for item in lst:
        result.append([int(max(item[0] / 1.2, MIN_INT)),
                       int(max(item[1] / 1.2, MIN_INT))])
    return result


def dimming_wave(lst):
    """
    creates a new list, every element in the original list gets a new value -
    the average of itself and its sequential indexes
    :param lst: a list
    :return: updated list
    """
    result = []
    for item in range(len(lst)):
        if item == 0:
            result.append(get_average_item(item, lst))
        elif item == len(lst) - 1:
            result.append(get_average_item(item - 1, lst))
        else:
            result.append(get_average_item(item, lst, True))
        print(result)
    return result


def combine_lists(list1, list2):
    """
    gets 2 lists, and creates a new list - every element is the rounded
    average of the right elements in the original lists
    :param list1: list no. 1
    :param list2: list no. 2
    :return: combined average list
    """
    return [
        int((list1[0] + list2[0]) / 2),
        int((list1[1] + list2[1]) / 2)
    ]


def max_min_lists(list1, list2, rates):
    """
    gives the longest and the shortest lists from 2 lists
    :param list1: list no. 1
    :param list2: list no. 2
    :return: longest and shortest lists
    """
    if list1[0] == rates[0]:
        return (list2[1], list1[1])
    else:
        return (list1[1], list2[1])


def find_gcd(number1, number2):
    """
    get the  greatest common divisor of two numbers
    :param number1: number1
    :param number2: number2
    :return: greatest common divisor of number1 and number2
    """
    return math.gcd(number1, number2)


def find_smp_rt(rt1, rt2):
    """
    determine the sample rates - highest and lowest
    :param rt1: list of the first file
    :param rt2: list of the second file
    :return: a tuple with the needed values of the sample rates
    """
    return (min(rt1, rt2), max(rt1, rt2))


def lst_combination(list1, list2):
    """
    gets 2 lists, and creates a new list - every needed element is the
    average of the right elements in the original lists, or the right element
    in the longer list
    :param list1: The list of the first file
    :param list2: The list of the second file
    :return: updated list of the combined file
    """
    upd_lst = []
    rates = find_smp_rt(list1[0], list2[0])  # lower & higher sample
    lists = max_min_lists(list1, list2, rates)
    max_list = lists[0]
    min_list = lists[1]
    l_smp_rt = rates[0]
    h_smp_rt = rates[1]
    # rates
    gcd = find_gcd(l_smp_rt, h_smp_rt)  # greatest common divisor
    counter = 0
    min_list_index = 0

    for i in range(len(max_list)):
        if counter < int(l_smp_rt / gcd):
            if len(min_list) <= min_list_index:
                upd_lst.append(max_list[i])
            else:
                upd_lst.append(
                    combine_lists(max_list[i], min_list[min_list_index]))
                min_list_index += 1
            counter += 1
        elif counter < int(h_smp_rt / gcd):
            counter += 1

        if counter == int(h_smp_rt / gcd):
            counter = 0

    return (l_smp_rt, upd_lst)


def get_sample_per_cycle(rate, freq):
    """
    calculate the samples per cycle
    :param rate: sample rate value
    :param freq: sample rate value
    :return: samples per cycle
    """
    if freq == 0:
        return 0
    return rate / freq


def get_sample(max_volume, rate, freq, index):
    """
    calculate the sample value per index
    :param max_volume: maximum volume
    :param rate: sample rate value
    :param freq: sample rate value for note
    :param index: the needed index in the list
    :return: overall sample
    """
    if freq == 0:
        return 0
    return int(max_volume * (
        math.sin(math.pi * 2 * (index / get_sample_per_cycle(rate, freq)))))


def read_melody_file(fileName):
    """
    this function reads the composing file
    :param fileName: composing file
    :return: the list of the composed tune
    """
    result = []
    try:
        with open(fileName, 'r') as f:
            for ln in f.readlines():
                splitLine = ln.split()
                for i in range(len(splitLine[0::2])):
                    result.append((splitLine[i * 2], splitLine[i * 2 + 1]))

    except IOError:
        print("Could not read file:", fileName)
    except:
        print("Could not read file:", fileName)

    return result


def get_note_lst(rate, freq):
    """
    this function gets the note list
    :param rate: value rate
    :param freq: frequency rate
    :return: list of the notes
    """
    result = []
    full_rate = rate * 125
    for i in range(full_rate):
        result.append([get_sample(MAX_INT, FRAME_RATE, freq, i),
                       get_sample(MAX_INT, FRAME_RATE, freq, i)])
    return result


def list_to_melody(lst):
    """
    Turn list to melody
    :param lst: list of tuples represent note and rate
    :return: the needed melody as a list
    """
    result = []
    for item in lst:
        result.extend(get_note_lst(int(item[1]), MusicalNoteFreq[item[0]]))
    return result


def read_files(path, melody=False, two=False):
    """
    this function reads the needed files
    :param path: file path
    :param melody: if melody file
    :param two: If two files
    :return:
    """
    result = []
    if melody:
        return read_melody_file(path)
    else:
        if two:
            for item in path.split():
                load_file = wave_helper.load_wave(item)
                if load_file == -1:
                    return -1
                else:
                    result.append(load_file)
            return result
        else:
            load_file = wave_helper.load_wave(path)
            return load_file


def get_files_from_user(melody=False, two=False):
    """
    this function gets the files from the user as an input
    :param melody: If melody file
    :param two: If two files
    :return: the files as lists
    """
    stop = False
    files = []
    while not stop:
        input_file = input("Enter file/s: ")
        files = read_files(input_file, melody, two)
        if files != -1:
            if len(files) != 2 and two:
                print("Two files where asked")
            else:
                # for file in files:
                #     for item in file:
                #         if item == []:
                #             continue
                #         for char in item:
                #             if not char.isdigit():
                #                 continue
                stop = True
        else:
            print("File does not exist")
    return files


def compose_file():
    """
    Compose file from filename
    :param filename: filename path
    :return: composed file
    """
    return (FRAME_RATE, list_to_melody(get_files_from_user(melody=True)))


def combine_audio():
    """
    this function is combining the audio
    :return: the combined audio as a list
    """
    files = get_files_from_user(melody=False, two=True)
    return lst_combination(files[0], files[1])


def edit_audio(input_lst=None):
    """
    the central function for editing the audio, according to the users choise
    :param file_lst:
    :return: the edited audio
    """
    stop = False
    print("Edit Audio Menu:")
    while not stop:
        if input_lst == None:
            file_lst = get_files_from_user()
        else:
            file_lst = input_lst
        rate = file_lst[0]
        print("For reverse audio press 1")
        print("For accelerate audio press 2")
        print("For slowing audio press 3")
        print("For increasing audio press 4")
        print("For decreasing audio press 5")
        print("For dimming audio press 6")
        print("For exit press 7")
        response = input("Your choice: ")
        if response.isdigit():
            response = int(response)
        if response == 1:
            file_lst = reverse_wave(file_lst[1])
        elif response == 2:
            file_lst = speed_wave(file_lst[1])
        elif response == 3:
            file_lst = slow_wave(file_lst[1])
        elif response == 4:
            file_lst = increase_wave(file_lst[1])
        elif response == 5:
            file_lst = decrease_wave(file_lst[1])
        elif response == 6:
            file_lst = dimming_wave(file_lst[1])
        else:
            print("Common be serious, enter valid input")
            continue

        return (rate, file_lst)


def save_wav_file(rate, lst):
    """
    this function is saving the file with a new name
    :param rate: the updated rate value
    :param lst: the updated list
    """
    fn = input("Get output file name: ")
    wave_helper.save_wave(rate, lst, fn)


def passage_menu(lst):
    """
    the menu that managing the users preference: to save or to change the file
    :param lst:
    """
    stop = False
    while not stop:
        print("For save audio press 1")
        print("For edit audio press 2")
        response = input("Your choice: ")
        if response.isdigit():
            response = int(response)
        if response == 1:
            print(lst)
            if (len(lst) == 2):
                rate = int(lst[0])
                audio_list = lst[1]
            else:
                rate = FRAME_RATE
                audio_list = lst
            save_wav_file(rate, audio_list)
            stop = True
        elif response == 2:
            edit_audio(lst)
            stop = True
        else:
            print("Common be serious, enter valid input")


def full_main():
    """
    the main function, gets all the code together
    """
    stop = False
    print("Main Menu:")
    while not stop:
        print("For edit audio press 1")
        print("For merge audio press 2")
        print("For compose audio press 3")
        print("For exit 4")
        response = input("Your choice: ")
        if response.isdigit():
            response = int(response)

        if response == 1:
            result = edit_audio()
        elif response == 2:
            result = combine_audio()
        elif response == 3:
            result = compose_file()
        else:
            if response == 4:
                stop = True
            else:
                print("Common be serious, enter valid input")
            continue

        passage_menu(result)


if __name__ == '__main__':
    full_main()
