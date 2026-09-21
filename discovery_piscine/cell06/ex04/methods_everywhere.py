#!/usr/bin/env python3

import sys

def shrink(string):
    print(string[:8])

def enlarge(string):
    while len(string) < 8:
        string += "Z"
    print(string)

if len(sys.argv) < 2:
    print("none")
else:
    for string in sys.argv[1:]:
        if len(string) > 8:
            shrink(string)
        elif len(string) < 8:
            enlarge(string)
        else:
            print(string)