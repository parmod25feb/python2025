# Python program to check if the User input is a Prime number or not

num1 = eval(input("Pls enter your number : "))

def checkifprimenumber(num):
    value=True
    for i in range(2,num):
        print(i,end=",")
        if num%i == 0:
            value=False
            break
    return value
bool = checkifprimenumber(num1)
if bool:
    print("Number {} is Prime number ".format(num1))
else:
    print("Number {} is NOT a Prime number ".format(num1))
