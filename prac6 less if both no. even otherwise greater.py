
num1 = int(input("Enter first number : " ))
num2 = int(input("Enter second number : "))

if(num1%2==0 and num2%2==0):
    # both numbers are even
    print("Smaller number of the two entered numbers is : ",min(num1,num2))
else:
    # if entered numbers are odd or one of them is odd
    print("Larger of the two entered numbers is : ",max(num1,num2))    