# Q: Implement a function to check if a linked list is a palindrome
# input: linked list containing nodes of 1 letter
# output: boolean, return true if palindrome, false if not


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

# compare the reverse list to the original list
def compare_list(list_a, list_b):
    while list_a != None and list_b != None:
        # if lists are the same return true, else return false
        if list_a.data != list_b.data:
            return False
        list_a = list_a.next
        list_b = list_b.next
    return True


list_a = SLinkedList()
list_a.addNode('R')
list_a.addNode('A')
list_a.addNode('C')
list_a.addNode('E')
list_a.addNode('C')
list_a.addNode('A')
list_a.addNode('R')

list_a.printList()

reversed_list = SLinkedList()
# list_a_reverse = reverse_list(list_a.head)
reverse_list(list_a.head,reversed_list)
# list_a_reverse.printList()
reversed_list.printList()

print(compare_list(list_a.head,reversed_list.head))


