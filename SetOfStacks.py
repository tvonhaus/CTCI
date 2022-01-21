

class SetOfStacks():
    def __init__(self):
        self.stack_list = []
        self.current_stack = Stack()

    def __str__(self):
        out = ""
        for stack in self.stack_list:
            out += str(stack)
            out += "\n"
        return out

    def push(self,new_node):
        if self.current_stack.getSize() == 5:
            new_stack = Stack()
            new_stack.push(new_node)
            self.stack_list.append(new_stack)
            self.current_stack = new_stack
        elif self.current_stack.isEmpty():
            self.current_stack.push(new_node)
            self.stack_list.append(self.current_stack)
        else:
            self.current_stack.push(new_node)
            self.stack_list[len(self.stack_list)-1] = self.current_stack

    def popAt(self,index):
        if self.stack_list[index].isEmpty():
            raise Exception("Attempting to pop from empty stack")
        self.stack_list[index].pop()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
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

node1 = Node(10)
node2 = Node(12)
node3 = Node(5)
node4 = Node(3)
node5 = Node(30)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
test_stack_set = SetOfStacks()

test_stack_set.push(node1)
test_stack_set.push(node2)
test_stack_set.push(node3)
test_stack_set.push(node4)
test_stack_set.push(node5)
test_stack_set.push(node6)
test_stack_set.push(node7)
test_stack_set.push(node8)
test_stack_set.push(node9)
test_stack_set.push(node10)
test_stack_set.push(node11)
print(test_stack_set)
test_stack_set.popAt(0)
print(test_stack_set)
test_stack_set.popAt(2)
print(test_stack_set)