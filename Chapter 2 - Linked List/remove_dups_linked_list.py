# Q: remove dups from a linked list without buffer
# input: linked list with dups potentially
# output: none, but we modified the list to be all unique

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def print_list(head_node):
    curr_node = head_node
    while curr_node != None:
        print(curr_node.data)
        curr_node = curr_node.next
        
# n is the number of nodes
# O(n^2) because we have nested traversals
# n + n-1 + n-2 + n-3 ... + 1 == n*(n-1)/2 ~= n*n/2 ~= n*n ~= O(n^2)
# O(1) because no buffer
def remove_dups(head_node):
    # loop thru the list
    curr_node = head_node
    while curr_node != None:
        # for a given curr_node i want to traverse the rest of the list 
        inner_node = curr_node.next
        prev_inner_node = curr_node
        while inner_node != None:
            # and remove any duplicates of that curr_node within that traversal
            if inner_node.data == curr_node.data:
                # DUPLICATE ALERT
                # remove them
                # prev_inner_node -> inner_node -> inner_node.next
                prev_inner_node.next = inner_node.next
            else:
                prev_inner_node = inner_node
                
            inner_node = inner_node.next
        curr_node = curr_node.next

# n are the number nodes
# O(n) time because we traverse the whole list in the worst case
# O(n) space becasue the set could be the size of the number of nodes in the worst case 
# 1 -> 2 -> 3 -> 5
def removeDups_buffer(head_node):
    seen_nodes = set()
    curr_node = head_node
    prev_node = None 
    while curr_node != None:
        print("Current node: " + curr_node.data)
        if curr_node.data in seen_nodes:
            #delete curr_node
            prev_node.next = curr_node.next
            # node1 -> curr_node -> node3
        seen_nodes.add(curr_node.data)
        prev_node = curr_node
        curr_node = curr_node.next
        
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

print("before")
print_list(node1)

remove_dups(node1)

print("after")
print_list(node1)
