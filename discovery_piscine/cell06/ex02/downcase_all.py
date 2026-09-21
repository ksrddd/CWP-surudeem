#!/usr/bin/env python3
import sys

def downcase_it(string):
    return string.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for string in sys.argv[1:]:
        print(downcase_it(string))