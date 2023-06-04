for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)


# for num in range(1, 101):
#     output = ""
#     if num % 3 == 0:
#         output += "FIZZ"
#     if num % 5 == 0:
#         output += "BUZZ"
#     if not output:
#         output = str(num)
#     print("{:<8}".format(output), end="")
#     if num % 10 == 0:
#         print()
