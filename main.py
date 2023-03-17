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
    return '-'

sentence = "test is really an important question that i have?"
words = sentence.split()

def initial_load():
    sentence = ''
    for word in words:
        sentence += check_string_in_files(word, "smart_dictionary") + " "
    print(sentence)
initial_load()
exit()
