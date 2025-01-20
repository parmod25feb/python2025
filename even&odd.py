# This is program to segregate the Even and odd numbers from a list
ls = [1,2,3,44,5,6,7,8,99,0]
# Printing the original list
print("Here is your list {}".format(ls))
# Function definition
def evenandodd(lst):
    even, odd =[], [] 
    for num in lst:    # Iterating through the list one by one
        if num%2==0:
            even.append(num)
        else:   
            odd.append(num)
        #num=0
    return even,odd
    
# Calling the function which will return 2 lists
nums = evenandodd(ls)
print("Even number list is : {}".format(nums[0]))
print("Odd number list is : {}".format(nums[1]))