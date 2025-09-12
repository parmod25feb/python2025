# This program is to implement the Queue Data Structure using Python List

queue =[]

def enqueue(data):
    queue.append(data)
    print(queue)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        queue.pop(0)
        print(queue)

while True:
    choice = int(input("\nPlease enter your choice : \n1. Add in queue \n2. Delete from queue \n3. Quit : \n"))
    if choice == 1:
        d = int(input("\nPlease enter the data : "))
        enqueue(d)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("\nPlease select the correct choice.")