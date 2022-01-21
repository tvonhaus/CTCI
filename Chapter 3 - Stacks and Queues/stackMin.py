# Q: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element
# push, pop and min should all operate in O(1) time

## Following operations:
# pop -> remove the top item from the stack
# push -> Add an item to the top of the stack
# peek -> return the top of the stack
# isEmpty -> return true if and only if the stack is empty


# to keep track of minimum could add an attribute to Stack class self.min
# upon addition of a new Node to the stack, should compare to the stacks current
# min, and if its less than current min, set stack.min to value of new node
# if stack is empty and first node is added, set min to first node
# function min() should return the stack's min


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        self.min = 99999999

    def __str__(self):
        curr = self.head
        out = ""
        while curr != None:
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

    # def push(self, new_node):
    #     if self.isEmpty():
    #         self.head = new_node
    #         # self.min = new_node.value
    #     # if new_node.value < self.min:
    #     #     self.min = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
    #     self.size += 1

    def push(self, new_node):
        if not self.isEmpty():
            new_node.next = self.head
            # self.min = new_node.value
        if new_node.value < self.min:
            self.min = new_node.value
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def min(self):
        return self.min.value

node1 = Node(10)
node2 = Node(12)
node3 = Node(5)
node4 = Node(3)
node5 = Node(30)

test_stack = Stack()

test_stack.push(node1)
print(test_stack)
print(test_stack.min)
test_stack.push(node2)
print(test_stack)
print(test_stack.min)
test_stack.push(node3)
print(test_stack)
print(test_stack.min)
test_stack.push(node4)
print(test_stack)
print(test_stack.min)
test_stack.push(node5)
print(test_stack)
print(test_stack.min)