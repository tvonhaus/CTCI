# Following operations:
# pop -> remove the top item from the stack
# push -> Add an item to the top of the stack
# peek -> return the top of the stack
# isEmpty -> return true if and only if the stack is empty

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        curr = self.head.next
        out = ""
        while curr:
            out += str(curr.value) + "->"
            curr = curr.next
        return out

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head

    def push(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

         

