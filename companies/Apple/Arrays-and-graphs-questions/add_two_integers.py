class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

# Linked List 1
node3 = Node(9) 

node2 = Node(9) 
node2.next = node3

node1 = Node(0) 
node1.next = node2

head1 = Node(1) 
head1.next = node1

# Linked List 2 
node5 = Node(2) 

node4 = Node(3) 
node4.next = node5

head2 = Node(7) 
head2.next = node4

# 19 % 10 => 

def add_two_integers(root1=head1, root2=head2):
    res = Node(0)
    tail = res
    remainder = 0

    while root1 or root2 or remainder:
        new_head = Node(0)
        numb1 = 0
        numb2 = 0
        
        if root1:
            numb1 = root1.value
            root1 = root1.next 
        if root2:
            numb2 = root2.value
            root2 = root2.next 
        total = numb1 + numb2 + remainder

        if total > 9:
            new_head.value = total % 10
            remainder = total // 10
        else:
            new_head.value = total
            remainder = 0

        tail.next = new_head
        tail = tail.next

    return res.next

def display_linked_list(root):
    while root:
        print(f"{root.value}", end=', ')
        root = root.next
    print(end='\n\n')

print("head 1:")
display_linked_list(head1)

print("head 2:")
display_linked_list(head2)

print("head 3:")
display_linked_list(add_two_integers(head1, head2))
