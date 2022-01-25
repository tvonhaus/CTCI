# Q: implement a MyQueue class which implements a queue using two stacks

# Stack = First in, last out
# Queue = First in, first out


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

    def push(self, new_node):
        if not self.isEmpty():
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


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        curr = self.stack1.head
        out = ""
        while curr != None:
            out += str(curr.value) + "->"
            curr = curr.next
        return out

    def isEmpty(self):
        return self.stack1.size == 0

    def push(self, new_node):
        if not self.isEmpty():
            new_node.next = self.stack1.head
        self.stack1.head = new_node
        self.stack1.size += 1

    # add values to first stack 1->2->3->4 pop and add to new stack
    # 4->3->2->1
    # pop from new stack to get value that should be popped from queue (4)
    # pop and add the remaining values back to the first stack
    def pop(self):
        if self.stack1.head == None:
            raise Exception("Popping from an empty queue")
        while self.stack1.head.next != None:
            self.stack2.push(new_node=Node(self.stack1.pop()))
        popped_node = self.stack1.head
        self.stack1.head = None
        while self.stack2.head != None:
            self.stack1.push(new_node=Node(self.stack2.pop()))
        return popped_node.value


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
test_queue = MyQueue()
test_queue.push(node1)
test_queue.push(node2)
test_queue.push(node3)
test_queue.push(node4)
test_queue.push(node5)
print(test_queue)
test_queue.pop()
print(test_queue)
test_queue.pop()
print(test_queue)
test_queue.pop()
print(test_queue)
test_queue.pop()
print(test_queue)
test_queue.pop()
print(test_queue)
