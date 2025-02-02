class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.left  = left
        self.right = right

        self.key = key 
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        # Essentials 
        self.capacity = capacity
        self.quantity = 0 
        self.hashmap = {int: Node} # key: Node

        # Setup
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
    
    def put(self, key: int, value: int) -> None:
        self.quantity += 1

        # Adding a new Node
        if key not in self.hashmap:
            newNode = Node(key=key, value=value)
            self.hashmap[key] = newNode  
            # Add new node - unfinished  
            if self.quantity == 1:
                self.head.right = newNode
                self.tail.left = newNode
                newNode.left = self.head
                newNode.right = self.tail
            elif self.quantity > 1:
                boiler = self.head.right # the node right after the head
                self.head.right = newNode 
                newNode.left = self.head
                newNode.right = boiler 
                boiler.left = newNode

        # Updating a current node
        else:
            # Updated the node and hashmap
            boiler = self.hashmap[key]
            boiler.value = value
            
            # Extract the node 
            leftNode    =  boiler.left
            rightNode   =  boiler.right
            leftNode.right = rightNode
            rightNode.left = leftNode

            # Insert the node 
            boiler_ = self.head.right  
            self.head.right = boiler
            boiler.left = self.head
            boiler.right = boiler_
            boiler_.left = boiler

        # H - n3' - n1 - n2 - T

        # Get rid of excessive nodes - Eviction
        if self.quantity > self.capacity:
            self.quantity -= 1 
            
            boiler = self.tail.left
            
            prev_node = boiler.left
            prev_node.right = self.tail
            self.tail.left = prev_node
            del self.hashmap[boiler.key]

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        boiler = self.hashmap[key]
            
        # Extract the node 
        leftNode    =  boiler.left
        rightNode   =  boiler.right
        leftNode.right = rightNode
        rightNode.left = leftNode

        # Insert the node 
        boiler_ = self.head.right  
        self.head.right = boiler
        boiler.left = self.head
        boiler.right = boiler_
        boiler_.left = boiler

        return boiler.value        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)