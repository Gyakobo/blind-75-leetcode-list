
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left  = left
        self.right = right
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


