first_num = int(input("Enter the first number: "))
sec_num = int(input("Enter the second number: "))
mult = first_num * sec_num

if mult > 0:
    print(first_num, "x", sec_num, "=", mult)
    print("The result is positive.")
elif mult < 0:
    print(first_num, "x", sec_num, "=", mult)
    print("The result is negative.")
else:
    print(first_num, "x", sec_num, "=", mult)
    print("The result is positive and negative.")
