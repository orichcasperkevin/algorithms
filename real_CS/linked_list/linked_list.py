# A single node of a singly Linked List
class Node:
  # constructor
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        if self.next:
            return f"{self.data}->{self.next.data}"
        else:
            return f"{self.data}->None"



# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = None


    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current)
            current = current.next

    def reverse(self):
        current = self.head
        previous = None
        next = self.head.next
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            if current:
                self.head = current    



# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)
LL.insert(7)
# LL.printLL()

LL.reverse()
print("____-")
LL.printLL()
