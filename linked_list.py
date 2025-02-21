class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  
        
    def insert(self, val):
        new_node = Node(val)

        if not self.head:  
            self.head = new_node
            return 
        
        temp = self.head 
        while temp.next: 
            temp = temp.next
        
        temp.next = new_node 

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")  



ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  
