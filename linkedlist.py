class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty.")
        else: 
            n = self.head
            while n is not None:
                print(n.data," -> ",end="")
                n=n.next
        print("\n")

    def addatbeginning(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node

    def addattheend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else: 
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def add_afteranode(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_beforenode(self,data,x):
        if self.head is None:
            print("Linked list is empty.")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next=self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.next= n.next
            n.next = new_node
    # def add_attheend(self,data):
    #     if self.head is None:
    #         print("Linked list is Empty")
    #         return
    #     else:
    #         n=self.head
    #         while n.next is not None:
    #             n = n.next
    #         new_node = Node(data)
    #         n.next = new_node

    def deletefrombeginning(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n=self.head
            n = n.next
            self.head = n

    def deletefromend(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.next is None:
            self.head = None  
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next=None

    def deleteagivennode(self,x):
        if self.head is None:
            print("Link list is emapty and node is not present.")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not present in the linked list")
        else:
            n.next= n.next.next
               

ll = Linkedlist()
ll.addatbeginning(10)
# ll.addatbeginning(20)
# ll.addatbeginning(30)
# ll.addattheend(100)
# ll.print_ll()
# ll.add_afteranode(40,10)
# ll.add_beforenode(500,10)
# ll.add_attheend(40)
# ll.add_attheend(50)
# ll.add_attheend(60)

ll.print_ll()
ll.deleteagivennode(10)
ll.print_ll()