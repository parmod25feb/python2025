# Program to print the fibonacci series

rng = int(input("Pls enter the max range to print the Fibonacci series : "))

def fibonacci_series(max):
    a,b=0,1
    c=0
    print("\n\nHere is the fibonacci series : ")
    while(c < max):
        print(c,end=",")
        a=b
        b=c
        c=a+b

fibonacci_series(rng)