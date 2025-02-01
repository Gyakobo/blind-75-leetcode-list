class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next 

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

def merge_two_sorted_linked_lists(list1, list2) -> Node:
    newHead = Node()
    pointer1 = list1
    pointer2 = list2
    pointer3 = newHead

    while pointer1 or pointer2:
        if pointer1 and pointer2 and pointer1.value >= pointer2.value:
            pointer3.next = pointer2
            pointer3 = pointer2
            pointer2 = pointer2.next

        elif pointer1 and pointer2 and pointer1.value < pointer2.value:
            pointer3.next = pointer1
            pointer3 = pointer1
            pointer1 = pointer1.next

        elif pointer1 and not pointer2:
            pointer3.next = pointer1
            pointer3 = pointer1
            pointer1 = pointer1.next

        elif pointer2 and not pointer1:
            pointer3.next = pointer2
            pointer3 = pointer2
            pointer2 = pointer2.next

    return newHead.next

print("head 1:")
display_linked_list(head1)

print("head 2:")
display_linked_list(head2)

print("head 3:")
display_linked_list(merge_two_sorted_linked_lists(head1, head2))