# Q: Two numbers represented by a linked list in reverse order. Sum them without
#    converting them into an integer.
# input: Two linked lists, a & b
# output: linked list of the sum of a & b in reverse order

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


# Must give sum_list function the head nodes of the two linked lists and not SLinkedList object
def sum_list(list_A,list_B):
    return_list = SLinkedList()
    carry = 0
    sum_val = 0
    # iterate through both the linked lists at the same time
    while list_A != None and list_B != None:
        print('Entered loop')
        a_value = list_A.data
        print(a_value)
        b_value = list_B.data
        print(b_value)
        if a_value == None:
            a_value = 0
        if b_value == None:
            b_value = 0
        print(a_value,b_value)
    #  sum the values of the two at each iteration, 
    #   check if there is a carry from the previous iteration
        sum_val = a_value + b_value + carry
    #       if there is a carry value: add a 1 to the sum
        print('Sum val: ',sum_val)
        print('carry: ',carry)
    #   if the sum is > 10, set the carry value to 1
        if sum_val >= 10:
            carry = 1
            # must add only ones digit of the sum to the output linked list
            sum_val = sum_val - 10
        #   if not set the carry value to 0 (carry value should start at 0 before iteration begins -> first sum will never have a carry)
        else:
            carry = 0
        #   Add the sum as a new node to the output linked list
        return_list.addNode(sum_val)
        list_A = list_A.next
        list_B = list_B.next
    return(return_list)
    # iterate until both the linked lists have reached node.next = null


## Testing
## Set up input lists
list_a = SLinkedList()
list_b = SLinkedList()
list_a.addNode(7)
list_a.addNode(1)
list_a.addNode(6)
list_b.addNode(5)
list_b.addNode(9)
list_b.addNode(2)


summed_list = sum_list(list_a.head,list_b.head)

print("Summed List: ")
summed_list.printList()