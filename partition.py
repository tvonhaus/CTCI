class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
        
class SLinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def addNode(self,new_node_val):
        new_node = Node(new_node_val)
        if self.head == None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new_node

# Q: Write code to partition a linked list around a value x, shuch that all nodes less than x come before all nodes greater than or equal to x
# input: value x to partition around
# output: linked list partitioned such that all values greater than/equal to x are on the right and
#         all values less than x are on the left


def partition(linked_list,x):
    curr_node = linked_list.head
    less_list = SLinkedList()
    greater_list = SLinkedList()
    # iterate through linked list
    while curr_node != None:
        # check if value is less than x: if true, add to "less than" list, if false add to "greater than" list
        if curr_node.data < x:
            less_list.addNode(curr_node.data)
        else:
            greater_list.addNode(curr_node.data)
        curr_node = curr_node.next
    curr_node = less_list.head
    while curr_node.next != None:
        curr_node = curr_node.next
    curr_node.next = greater_list.head
    return less_list
    # iterate through less than list and set its last node.next to the head node of greater than list


test_list = SLinkedList()
test_list.addNode(3)
test_list.addNode(5)
test_list.addNode(8)
test_list.addNode(5)
test_list.addNode(10)
test_list.addNode(2)
test_list.addNode(1)


partitioned_list = partition(test_list,5)
partitioned_list.printList()
