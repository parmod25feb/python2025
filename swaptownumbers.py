# Python program to swap two numbers without using third variable

num1 = eval(input("Enter 1st number : "))
num2 = eval(input("Enter 2nd number : "))
print("Original numbers before swap : {0}, {1}".format(num1,num2)) # Printing original numbers before swap

# Function to swap the numbers without using the 3rd variable.
def swap_numbers(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    return num1,num2

a,b =swap_numbers(num1,num2)  # Calling the function which returns the swapped numbers
print("Numbers after swap : {0}, {1}".format(a,b))   # Printing the numbers after swap