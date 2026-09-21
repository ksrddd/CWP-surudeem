#!/usr/bin/env python3

def array_of_names(person):
    names = []
    for first_name, last_name in person.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        names.append(full_name)
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))