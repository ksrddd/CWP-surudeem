num = int(input("Enter a number less than 25\n"))
i = num

if num > 25:
    print("Error")
else:
    while i <= 25:
        print("Inside the loop, my variable is", i)
        i += 1