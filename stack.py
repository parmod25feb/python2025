# This program is for Stack implementation in Python 

stack = []

def push_operation():
    item = int(input("Please eneter any number : "))
    stack.append(item)
    print(stack,end="\n")
def pop_operation():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print(f"Item {e} deleted from the stack")
    print(stack,end="\n")

while True:
    print("\nEnter your choice: \n1. Push an item in the stack \n2. Pop an item from the stack \n3. Quit")
    choice = int(input("Waiting for your choice : "))
    if choice == 1:
        push_operation()
    elif choice == 2:
        pop_operation()
    elif choice == 3:
        break
    else:
        print("\nEnter the correct operation\n")

