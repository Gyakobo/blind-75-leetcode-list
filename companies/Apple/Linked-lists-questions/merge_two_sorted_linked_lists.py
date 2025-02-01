class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

def display_linked_list(root):
    while root:
        print(f"{root.value}", end=', ')
        root = root.next
    print(end='\n\n')

# Linked List 1
node2 = Node(4) 

node1 = Node(2) 
node1.next = node2

head1 = Node(1) 
head1.next = node1

# Linked List 2 
node6 = Node(5) 

node5 = Node(4) 
node5.next = node6 

node4 = Node(3) 
node4.next = node5

head2 = Node(1) 
head2.next = node4

def merge_two_sorted_linked_lists(tail1, tail2):
    root = Node(None)
    head = root

    while tail1 or tail2:
        if tail1 and tail2 and tail1.value < tail1.value:
            head.next = tail1
            head = tail1

        elif tail1 and tail2 and tail1.value >= tail1.value:
            head.next = tail2
            head = tail2

        elif tail1 and not tail2:
            head.next = tail1
            head = tail1
        
        elif tail1 and not tail2:
            head.next = tail2
            head = tail2

        if tail1: tail1 = tail1.next
        if tail2: tail2 = tail2.next

    return root

print("head 1:")
display_linked_list(head1)

print("head 2:")
display_linked_list(head2)

print("head 3:")
display_linked_list(merge_two_sorted_linked_lists(head1, head2))