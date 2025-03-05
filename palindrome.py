# 9. Python program to check if the number is Palindrome or not

usr_num=eval(input("Please enter your number : "))

def ispalindrome(num):
    rev, rem =0,0
    while(num != 0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev

res= ispalindrome(usr_num)

if res == usr_num :
    print("Yes! number {0} is Palindrome ".format(usr_num))
else:
    print("Sorry! number {0} is NOT Palindrome ".format(usr_num))