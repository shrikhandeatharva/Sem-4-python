def print_square():
    while True:
        try:
            number = int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        else:
            square = number ** 2
            print(f"The square of {number} is {square}.")
            break

# Usage example:
print_square()
