class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        curr = self.head
        out = ""
        while curr:
            out += str(curr.value) + "->"
            curr = curr.next
        return out
        
    def isEmpty(self):
        return self.size == 0

    def add(self,value):
        curr = self.head
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            while curr.next != None:
                curr = curr.next
            curr.next = new_node

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        to_remove = self.head
        self.head = self.head.next
        return to_remove.value

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.head.value

    
    