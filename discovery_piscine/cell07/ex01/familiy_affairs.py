#!/usr/bin/env python3
def find_the_redheads(dupont_family):
    redheads = []
    for name, hair_color in dupont_family.items():
        if hair_color == "red":
            redheads.append(name)
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads((dupont_family)))