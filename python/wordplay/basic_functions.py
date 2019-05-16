"""
Basic functionality for this project (opening files, reading stuff etc)
"""

import os # operating system functions, like opening files and looking at stuff in directories


def read_file_basic(filename):
    f_in = open(filename)
    lines = f_in.readlines()
    f_in.close()
    return lines


def read_file(filename):
    """
    This method returns all the lines of a file as a list of strings.
    :param filename:
    :return: all the strings in a file
    """
    with open(filename, 'r') as f_in:  # this opens a file. we use this "with" syntax because that closes the file afterward
        lines = f_in.readlines()
    return lines


def list_files(directory):
    return os.list(directory)


def get_all_words_in_file(filename):
    """
    This method will open a file, read its contents, and return a dictionary of all words that occur and the number of times that they occur.
    :param filename:
    :return:
    """
    pass


def get_characters_in_file(filename):
    """
    This method returns all characters in the file
    :param filename:
    :return: a list of all characters in a filename
    """
    # we want to use a set for this rather than a list, because that gives us only the unique values.
    chars = set()
    lines = read_file(filename)
    for line in lines:
        for character in line:
            chars.add(character)
    return chars


def get_character_count_in_file(filename):
    """
    This method is intended to return a dictionary of characters mapped to the number of times they occur in
    the filename provided
    :param filename: the file to open
    :return: a dictionary in the form { character : number of times it occurs }
    """
    lines = read_file(filename)
    output_dict = {}  # we could also say output_dict = dict()
    for line in lines:
        for character in line:
            if character in output_dict:
                value = output_dict[character]
                new_value = value + 1
                output_dict[character] = new_value
            else:
                output_dict[character] = 1
    return output_dict


def get_most_common_character_in_file(filename):
    """
    Returns the character that occurs the most times in the file
    :param filename:
    :return:
    """
    character_counts = get_character_count_in_file(filename)
    maximum_count = 0
    maximum_character = None
    for k, v in character_counts.items():
        if v > maximum_count:
            maximum_count = v
            maximum_character = k
    return k


