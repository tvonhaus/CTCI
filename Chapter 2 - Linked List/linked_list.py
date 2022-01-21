

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
            
list = SLinkedList()

list.head = Node("Monday")
node_2 = Node("Tuesday")
node_3 = Node("Wednesday")

list.head.next = node_2
node_2.next = node_3

list.printList()
