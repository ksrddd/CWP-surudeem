#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    for string in sys.argv[1:]:
        if string.endswith("ism"):
            continue

        print(string + "ism")
