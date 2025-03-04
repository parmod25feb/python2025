# 6. Python program to reverse a number

user_num= eval(input("Please enter your number : "))

def number_reverse(num):
    rev,rem=0,0
    while num != 0:
        rem= num%10
        rev=rev*10+rem
        num= num//10
    return rev
    
rt_num=number_reverse(user_num)
print("Reverse of {0} is {1} ".format(user_num,rt_num))