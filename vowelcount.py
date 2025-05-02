#Write a Python function called count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) present in the string (case-insensitive).

# User will input the string
st= input("Please enter your string : ")

#Function definition
def vowel_count(st):
    count=0
    for ch in st:
        if ( ch == 'a' or ch == 'e' or ch == 'i' or ch=='o' or ch =='u'):
            count+=1
    return count

#Calling the function to count vowels in the string
num = vowel_count(st)

#Printing the result
print(f"Number of vowels are - {num} in the string - {st}")