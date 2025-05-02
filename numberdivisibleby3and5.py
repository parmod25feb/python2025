#Create a Python list containing the numbers from 1 to 100 (inclusive) that are divisible by both 3 and 5.

ls=[]
for num in range(1,101):
    if (num%3 == 0 and num%5==0):
        ls.append(num)

print(ls)