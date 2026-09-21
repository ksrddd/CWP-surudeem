#!/usr/bin/env python3
my_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for num in my_array:
    if num > 5:
        new_arr.append(num + 2)

print(my_array)
print(new_arr)