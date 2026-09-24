#!/usr/bin/env python3
first_num = int(input("Enter the first number: "))
sec_num = int(input("Enter the second number: "))
mult = first_num * sec_num

print(first_num, "x", sec_num, "=", mult)

if mult > 0:
    print("The result is positive.")
elif mult < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

