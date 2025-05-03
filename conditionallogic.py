'''Conditional Logic: Write a Python function called check_grade that takes a student's score 
as input and returns their corresponding grade based on the following scale:

90 or above: "A"
80-89: "B"
70-79: "C"
Below 70: "F"'''

grd = eval(input("Pls enter your grade (1-100) : "))

def grade_logic(grd):
    if (grd >=90 ):
        print(f"Congratulations your grade is : A")
    elif(grd >= 80 and grd <=  89):
        print(f"Congratulations your grade is : B")
    elif(grd >= 70 and grd <= 79):
        print(f"Your grade is : C")
    elif grd <70:
        print(f"Sorry! your grade is : Fail")
    else:
        print("Pls enter the correct choice.")

grade_logic(grd)