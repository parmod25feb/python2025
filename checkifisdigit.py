# 8. Python program to find the number of digits in a given number

st = input("Please enter your string (e.g : a1b2c3): ")

def check_if_isdigit(st):
    ls=[]
    for ch in st:
        if ch.isdigit():
            ls.append(ch)
    return ls

lst=check_if_isdigit(st)
hr=''.join(lst)
print(hr)
