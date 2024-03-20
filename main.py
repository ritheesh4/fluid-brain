from sys import exit
import re
import os
import random
brain_doubts = ''
doubt_words = []

# Check the input is number or float.


def check_it_is_number_or_float(value):
    if value.isalpha():
        return False
    global value_to_process
    value_to_process = 0
    try:
        if "." in value:
            value_to_process = float(value)
        else:
            value_to_process = int(value)
    except:
        return False

    if isinstance(value_to_process, float):
        return 'float'
    if isinstance(value_to_process, int):
        return 'number'
    if isinstance(10, int):
        print('reached hrere1', value_to_process)
        return 'number'
    else:
        return False

# Remove special characters from the given string


def remove_speical_character(string):
    return re.sub(r'\W+', '', string)

# Check the current string is present or not in the smart dictionary


def check_string_in_files(string, directory):
    # Get a list of all the files in the directory
    files = os.listdir(directory)
    # Loop through each file
    for file_name in files:
        # Check if the file is a text file
        if file_name.endswith(".txt"):
            # Open the file and read its contents
            with open(os.path.join(directory, file_name), "r") as file:
                contents = file.read()
                pattern = re.compile(r'\b{}\b'.format(string), re.IGNORECASE)
                # Check if the string is present in the file
                if re.search(pattern, contents):
                    return file_name[:-4]
    words_file = open("./main_dictionary/words.txt", "r")
    words_list = words_file.read()
    word_pattern = re.compile(
        r'\b{}\b'.format(string), re.IGNORECASE)
    if re.search(word_pattern, words_list):
        return 'word'
    return False

# Main function that checks the user input


def initial_load(sentence):
    global brain_doubts
    words = sentence.split()
    type_of_words_output = ''
    for word in words:
        dictionary_output = check_string_in_files(
            remove_speical_character(word), "smart_dictionary")
        if dictionary_output is False:
            dictionary_output = check_it_is_number_or_float(word)
            if dictionary_output is False:
                doubt_words.append(word)
                dictionary_output = '-'
        type_of_words_output += dictionary_output + " "

    if len(doubt_words) > 0:
        brain_doubts = 'I have some doubts. Can you tell me the meaning of these words'
    return type_of_words_output


while True:
    try:
        with open("./sentence_dictionary/coversation_starter.txt", "r") as file:
                sentences = file.readlines()
                sentences = [s.strip() for s in sentences]
                sentences = [s for s in sentences if s]
                random_sentence = random.choice(sentences)
                input_data = input(
                   random_sentence)
                response = initial_load(input_data)
                if len(doubt_words) > 0:
                    print(brain_doubts)
                    print(doubt_words)
                print("This is the analysed output.\n")
                print(response)
    except ValueError:
        print("Invalid input, please enter a number.")
