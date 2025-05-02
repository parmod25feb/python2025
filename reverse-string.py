# Write a Python function called reverse_string that takes a string as input and returns its reversed version.

st1=input("Please enter your string : ")
print(st1)
def reverse_string(st):
    rst=""
    for ch in st:
        rst=ch+rst
    return rst

res= reverse_string(st1)

print(f"Reverse of the string - {st1} is - {res}")