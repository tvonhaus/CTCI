# Q: Given two singly linked lists, determine if the two lists intersect. Return the intersecting node
# intersection is based on reference not value.
# input: two singly linked list heads
# output: the intersecting node of the two singly linked lists

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

# reverse the list
def reverse_list(head,reversed_list):
    #can use recursion to create a function that returns the list in reverse
    # recursion should close when curr_node.next = None
    # if current node.next is not none it should call the reverse function again with current_node.next as param
    if head.next != None:
        reverse_list(head.next,reversed_list)
    # when next is None, add the current node to new list reverse_list
    reversed_list.addNode(head.data)

#   1 -> 2 -> 3 -> 4 -> 5 -> 6
# A -> B -> C -> D ^
def listLength(list_head):
    count = 0
    while list_head != None:
        list_head = list_head.next
        count += 1
    return count

# O(N^2) method
# using i as the current node of the first linked list
# using j as the current node of the second linked list
# use nested loops to check whether i is equivalent to any of the nodes in j
# this is not very efficient

# O(N) method
# if there's an intersection the last nodes of both lists will be the same until the intersection is reached
# check to see if the last node of the lists is the same, if not, no intersection
def find_intersection(list_a,list_b):
    current_a = list_a.head
    current_b = list_b.head
    while current_a.next != None: 
        current_a = current_a.next
    while current_b.next != None:
        current_b = current_b.next
    if current_a != current_b:
        return("No intersection")
    # find lengths of both lists
    length_a = listLength(list_a.head)
    length_b = listLength(list_b.head)
    # if list lengths are different, find lengths of both lists and move up the longer list by difference in lengths to make them same length
    if length_a != length_b:
        difference = length_a - length_b
        if difference > 0:
            while difference != 0:
                list_a.head = list_a.head.next
                difference -= 1
        elif difference < 0:
            while difference != 0:
                list_b.head = list_b.head.next
                difference += 1
    # lists are now the same length
    # if lists are the same length, can just loop through the lists until i and j nodes are the same and return
    current_a = list_a.head
    current_b = list_b.head
    while current_a != current_b:
        current_a = current_a.next
        current_b = current_b.next
    return current_a.data





list_a = SLinkedList()
list_b = SLinkedList()


list_a.head = Node('A')
A_2 = Node('B')
A_3 = Node('C')
A_4 = Node('D')
A_5 = Node('E')
list_a.head.next = A_2
A_2.next = A_3
A_3.next = A_4
A_4.next = A_5


list_b.head = Node('1')
B_2 = Node('2')
B_3 = Node('3')
list_b.head.next = B_2
B_2.next = B_3
B_3.next = A_3

print('List A:')
list_a.printList()
print(listLength(list_a.head))
print('List B:')
list_b.printList()
print(listLength(list_b.head))

print(find_intersection(list_a,list_b))

