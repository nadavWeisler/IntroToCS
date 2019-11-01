#############################################################
# FILE : ex11.py
# WRITER : Nadav Weisler , weisler , 316493758
# EXERCISE : intro2cs ex11 2019
# DESCRIPTION:
#############################################################
from itertools import combinations


class Node:
    def __init__(self, data, pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def is_leaf(self):
        """
        Function that return if the node is leaf
        :return: boolean
        """
        if self.positive_child is None or self.negative_child is None:
            return True
        else:
            return False

    def diagnose(self, symptoms):
        """
        Diagnose from symptoms
        :param symptoms: string list
        :return: illness
        """
        if self.positive_child is None or self.negative_child is None:
            return self.data
        else:
            if self.data in symptoms:
                return self.positive_child.diagnose(
                    symptoms)
            else:
                return self.negative_child.diagnose(
                    symptoms)

    def illness_path_list(self, illness, lst=[], all_lst=[]):
        """
        Get all root path
        :param illness: string
        :param lst: list
        :param all_lst: list
        :return: illness path in Node
        """
        if self.is_leaf():
            if self.data == illness:
                all_lst.append(lst)
        else:
            self.positive_child.illness_path_list(illness,
                                                  lst + [True],
                                                  all_lst)
            self.negative_child.illness_path_list(illness,
                                                  lst + [False],
                                                  all_lst)
            return all_lst

    def get_all_symptoms(self, lst=[]):
        """
        Get all symptoms from Node
        :param lst: list
        :return: symptoms list
        """
        if self.is_leaf():
            return lst
        else:
            lst.append(self.data)
            self.positive_child.get_all_symptoms(lst)
            self.negative_child.get_all_symptoms(lst)
            return lst

    def get_illnesses_dictionary(self, dic={}):
        """
        Get illnesses dictionary count from root
        :param dic: dictionary
        :return: dictionary
        """
        if self.positive_child is None or self.negative_child is None:
            if self.data in dic.keys():
                dic[self.data] += 1
            else:
                dic[self.data] = 1
            return dic
        else:
            self.positive_child.get_illnesses_dictionary(dic)
            self.negative_child.get_illnesses_dictionary(dic)
            return dic

    def same_tree(self, other):
        if self.data != other.data:
            return False
        if not self.positive_child or not other.positive_child:
            if not self.positive_child and not other.positive_child:
                return True
            return False
        if not self.positive_child.same_tree(other.positive_child):
            return False
        if not self.negative_child.same_tree(other.negative_child):
            return False
        return True

    def print_tree(self, level=1, answer=''):
        print('    ' * (level - 1) + str(answer) + '+---' * (
                level > 0) + self.data)
        if self.positive_child:
            if self.positive_child:
                self.positive_child.print_tree(level + 1, 'P')
            if self.negative_child:
                self.negative_child.print_tree(level + 1, 'N')


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose(self, symptoms):
        """
        Diagnose illness with given symptoms
        :param symptoms: list of string
        :return: string
        """
        return self.root.diagnose(symptoms)

    def calculate_success_rate(self, records):
        """
        Calculate success rate from given records
        :param records: Record list
        :return: number
        """
        success_count = 0
        for record in records:
            if self.diagnose(record.symptoms) == record.illness:
                success_count += 1
        return success_count / len(records)

    def all_illnesses(self):
        """
        return all illnesses in tree
        :return: list of string
        """
        illnesses_dic = self.root.get_illnesses_dictionary()
        return sorted(illnesses_dic, key=illnesses_dic.get)

    def difference(self, other):
        """
        return differences between Diagnosers
        :param other: Diagnoser
        :return: string
        """
        combine_symptoms = set(self.root.get_all_symptoms() +
                               (other.root.get_all_symptoms()))
        combine_symptoms = list(combine_symptoms)
        all_combinations = sum(
            [list(map(list, combinations(combine_symptoms, i))) for i in
             range(len(combine_symptoms) + 1)], [])

        for comb in all_combinations:
            if self.diagnose(comb) != other.diagnose(comb):
                return comb

    def paths_to_illness(self, illness):
        """
        Return all path to illnesses
        :param illness: string
        :return: boolean list
        """
        return self.root.illness_path_list(illness)


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


def get_record_dic_by_sym(records, symptoms):
    result = {}
    for record in records:
        result[record] = len(list(set(record.symptoms).intersection(symptoms)))
    return result


def get_empty_record_dic(records):
    """
    Get empty dictionary of all illnesses in records
    :param records: Record list
    :return: dictionary
    """
    result = {}
    for record in records:
        if not record.illness:
            continue
        if record.illness not in result.keys():
            result[record.illness] = 0
    return result


def get_fit_illness_from_symptoms(records, pos_symptoms, neg_symptoms):
    """
    Get fitted illness for records by positive and negative symptoms
    :param records: Record list
    :param pos_symptoms: string list
    :param neg_symptoms: string list
    :return: illness
    """
    records_dic = get_empty_record_dic(records)
    for record in records:
        if get_common_count(neg_symptoms, record.symptoms) > 0:
            continue
        elif len(pos_symptoms) != get_common_count(pos_symptoms,
                                                   record.symptoms):
            continue
        elif not record.illness:
            continue
        else:
            records_dic[record.illness] += 1

    sorted_list = sorted(records_dic, key=records_dic.get)
    return sorted_list[-1]


def get_common_count(list1, list2):
    """
    Get count of common between two lists
    :param list1: list
    :param list2: list
    :return: number
    """
    return len(list(set(list1).intersection(list2)))


def build_tree(records, symptoms, pos_lst=[], neg_lst=[]):
    """
    Build tree function
    :param records: Record list
    :param symptoms: string list
    :param pos_lst: list
    :param neg_lst: list
    :return: Node
    """
    if symptoms == []:
        return Node(get_fit_illness_from_symptoms(records, pos_lst, neg_lst))

    if len(symptoms) == 1:
        new_node = Node(symptoms[0],
                        build_tree(records, [], pos_lst + [symptoms[0]],
                                   neg_lst),
                        build_tree(records, [], pos_lst,
                                   neg_lst + [symptoms[0]]))
    else:
        new_node = Node(symptoms[0],
                        build_tree(records, symptoms[1:],
                                   pos_lst + [symptoms[0]], neg_lst),
                        build_tree(records, symptoms[1:], pos_lst,
                                   neg_lst + [symptoms[0]]))

    return new_node


def optimal_tree(records, symptoms, depth):
    """
    Get optimal tree by records symptoms and depth
    :param records: Record list
    :param symptoms: string list
    :param depth: number
    :return: Node
    """
    comb = combinations(symptoms, depth)
    count = 0
    optimal = None
    for item in comb:
        current_tree = build_tree(records, item)
        current_diagnose = Diagnoser(current_tree)
        success_rate = current_diagnose.calculate_success_rate(records)
        if success_rate > count:
            count = success_rate
            optimal = current_tree
    return optimal


if __name__ == "__main__":

    # Manually build a simple tree.
    #                cough
    #          Yes /       \ No
    #        fever           healthy
    #   Yes /     \ No
    # influenza   cold

    flu_leaf = Node("influenza", None, None)
    cold_leaf = Node("cold", None, None)
    inner_vertex = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf = Node("healthy", None, None)
    root = Node("cough", inner_vertex, healthy_leaf)

    diagnoser = Diagnoser(root)

    # Test 1
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "cold":
        print("Test 1 passed")
    else:
        print("Test 1 failed. Should have printed cold, printed: ", diagnosis)

    # Test 2
    records = []
    records.append(Record("healthy", []))
    records.append(Record("influenza", ["cough", "fever", "sneezing"]))
    records.append(Record("dead", ["cough", "fever", "sneezing"]))
    records.append(Record("influenza", ["cough", "fever"]))
    records.append(Record("influenza", ["cough", "fever"]))
    records.append(Record("cold", ["cough", "sneezing"]))
    records.append(Record("influenza", ["cough"]))
    records.append(Record("dead", ["fever"]))
    records.append(Record("dead", ["fever"]))
    records.append(Record("healthy", ["fever"]))
    records.append(Record("healthy", ["fever"]))
    records.append(Record("dead", ["fever"]))
    records.append(Record("cold", ["fever"]))
    records.append(Record("cold", ["fever"]))
    records.append(Record("cold", []))
    records.append(Record("healthy", []))
    records.append(Record("cold", []))
    records.append(Record("cold", []))
    records.append(Record("healthy", []))
    records.append(Record("healthy", []))

    success_rate = diagnoser.calculate_success_rate(records)
    if success_rate == 0.5:
        print("Test 2 passed")
    else:
        print("Test 2 failed. Should have printed 0.5, printed: ",
              str(success_rate))

    # Test 3
    all_illness = diagnoser.all_illnesses()
    if all_illness == ['influenza', 'cold', 'healthy']:
        print("Test 3 passed")
    else:
        print(
            "Test 3 failed. Should have printed " +
            "['influenza', 'cold', 'healthy'], printed: ",
            str(all_illness))

    # Test 4
    flu_leaf2 = Node("influenza", None, None)
    cough_leaf2 = Node("cough", None, None)
    inner_vertex2 = Node("fever", flu_leaf, cold_leaf)
    healthy_leaf2 = Node("healthy", None, None)
    root2 = Node("cold", inner_vertex, healthy_leaf)

    diagnoser2 = Diagnoser(root2)
    diff = diagnoser.difference(diagnoser2)
    if diff == ['cough'] or diff == ['cold']:
        print("Test 4 passed")
    else:
        print(
            "Test 4 failed. Should have printed ['cough'], printed: ",
            str(diff))

    # Test 5
    illness_path = diagnoser.paths_to_illness("healthy")
    if illness_path == [[False]]:
        print("Test 5 passed")
    else:
        print(
            "Test 5 failed. Should have printed [[False]], printed: ",
            str(illness_path))

    # Test 6:

    influenza3 = Node("influenza")
    cold3 = Node("cold")
    dead3 = Node("dead")
    healthy3 = Node("healthy")

    fever3_plus = Node("fever", influenza3, cold3)
    fever3_minus = Node("fever", dead3, healthy3)
    cough_leaf3 = Node("cough", fever3_plus, fever3_minus)

    new_tree = build_tree(records, ["cough", "fever"])
    if new_tree.same_tree(cough_leaf3):
        print("Test 6 passed")
    else:
        print("Test 6 failed. Should have printed: ")
        cough_leaf3.print_tree()
        print("printed: ")
        new_tree.print_tree()

    # Test 7

    optimal = optimal_tree(records, ["cough", "sneezing", "fever"], 2)
    if optimal.same_tree(cough_leaf3):
        print("Test 7 passed")
    else:
        print("Test 7 failed. Should have printed: ")
        cough_leaf3.print_tree()
        print("printed: ")
        optimal.print_tree()
