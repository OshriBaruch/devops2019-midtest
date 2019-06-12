#!/usr/bin/env python3

#from muitiprocessing import Pool
import sys
import os

# prints if there is too meny arguments
def exit_file():
    print("Improper use")
    print("Usage: " + sys.argv[0] + " <dir> and <word>")

# checking if the number of arguments is valid right
if len(sys.argv) != 3:
    exit_file()
    sys.exit(1)
if (not os.path.isdir(sys.argv[1])):
    exit_file()
    sys.exit(1)

path = sys.argv[1]
word = sys.argv[2]

#Search the word in the line and print the file name
def print_if_word_exist(line,file_name):
    if word.lower() in line.lower():
        print (file_name)

# Open file and call to print_if_word_exist with lines
def set_searching(file_name):
    with open(file_name) as file:
        for line in file:
            print_if_word_exist(line,file_name)

# Recursive func to get all files
if __name__ == '__main__':
    for folder, subfolders, files in os.walk(path):
        for file in files:
            file_path = os.path.join(os.path.abspath(folder), file)
            set_searching(file_path)

