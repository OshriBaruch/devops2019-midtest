#!/usr/bin/env python3

import sys

def exit_file():
    print("Not right arguments")
    print("Usage: " + sys.argv[0] + " <String>")

# checking the the number of arguments is valid right
if len(sys.argv) != 2:
    exit_file()
    sys.exit(1)

#Defines variables
string = str(sys.argv[1])
d = {}

#Set key-value to dictionary
def set_key_value_in_dictionary(key):
    if not key in d:
        d[key] = string.index(key)

if __name__ == '__main__':
    for s in string:
        set_key_value_in_dictionary(s)
    print(d)
