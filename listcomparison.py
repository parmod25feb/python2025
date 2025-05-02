'''List Comprehension: Use list comprehension to create 
a new list containing only the even numbers from the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].'''

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list is : {num}")
def list_comparison(nm):
    ls=[]
    for item in nm:
        if (item%2==0):
            ls.append(item)
    return ls

rlst = list_comparison(num)
print(f"Here is the result list with even numbers : {rlst}")