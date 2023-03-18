from sys import exit
import re
import os

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
        return 'words'
    return '-'

sentence_file = open("./test_files/test_sentence.txt", "r")
sentence = sentence_file.read()
words = sentence.split()

def initial_load():
    type_of_words_output = ''
    for word in words:
        type_of_words_output += check_string_in_files(
            word, "smart_dictionary") + " "
    print(type_of_words_output)

initial_load()
exit()
