# 7. Python program to check if the user entered number is armstrong number or not

u_num = eval(input("Please enter your number : "))

def check_if_armstrongnumber(num):
    rem,arm=0,0
    while(num !=0 ):
        rem = num%10
        arm = arm+ rem**3
        num= num//10
    return arm

res = check_if_armstrongnumber(u_num)

if u_num == res:
    print("Yay! number is {0} is armstrong".format(u_num))
else:
    print("Sorry! number is not armstrong")