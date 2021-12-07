# Q: Delete a node in the middle of a singly linked list given only the node
# input: the node c from the linked list a -> b -> c -> d -> e -> f

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head_node):
    curr_node = head_node
    while curr_node != None:
        print(curr_node.data)
        curr_node = curr_node.next

# link nodes before given node to nodes after given node
# replace given node with given_node.next, given_node.next with node after, etc until end of list has been reached
# a -> b -> c -> d -> e -> f
# a -> b -> d -> d -> e -> f
# a -> b -> d -> e -> e -> f
# a -> b -> d -> e -> f -> f
# when currNode.next is None, delete currNode


def deleteMiddle(given_node):
# assume the node that's been given is in the middle of the list
# a -> b -> c -> d -> e -> f
# replace given node with given_node.next, given_node.next with node after, etc until end of list has been reached
# start loop as current node at given node
# repeat until current_node.next.next is None and then delete current_node.next 
    current_node = given_node
    while current_node.next.next != None:
        # set current_node.data = current_node.next.data
        current_node.data = current_node.next.data
        # a -> b -> d(current) -> d(current.next) -> e -> f
        # set current_node equal to current_node.next
        current_node = current_node.next
        # a -> b -> d -> d(current) -> e -> f
    # set current to next.data and delete current_node.next
    current_node.data = current_node.next.data
    current_node.next = None
    
    

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

print('Before:')
print_list(node1)

deleteMiddle(node3)
print('After:')
print_list(node1)


