class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class DirectedGraph:
    def __init__(self, edges):
        self.nodes = {}
        self.build_graph(edges)
    
    def build_graph(self, edges):
        for start, end in edges:
            if start not in self.nodes:
                self.nodes[start] = Node(start)
            if end not in self.nodes:
                self.nodes[end] = Node(end)
            
            self.nodes[start].neighbors.append(self.nodes[end])

    def get_root_node(self):
        return self.nodes.get(0, None)

    def display_graph(self):
        for node in self.nodes.values():
            print(f"Node {node.value}: {[neighbor.value for neighbor in node.neighbors]}")

# Template edges
template = [ [0, 4], [4, 0], [4, 3], [0, 3], [3, 2], [4, 1], [1, 2], [2, 0], [0, 2] ]

print("Create the Original Graph")
graph = DirectedGraph(template)
graph.display_graph()

'''
# Time complexity: O(n)
print("Cloning the Graph")
def clone_directed_graph(root: Node) -> Node:
    oldToNew = {Node: Node} # Mapping Old nodes to new ones

    def dfs(head):
        if head in oldToNew:
            return oldToNew[head]
            
        copy = Node(head.value)
        oldToNew[head] = copy

        for nei in head.neighbors: 
            copy.neighbors.append(dfs(nei))
        
        return copy

    # Run the Depth First Search and return the 
    return dfs(root) if root else None
    
clone = clone_directed_graph(graph.get_root_node())
'''

def display_dependency_graph(root):
    if not root:
        print("No root node provided.")
        return
    
    visited = set()
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node.value in visited:
            continue
        
        visited.add(node.value)
        print(f"Node {node.value} depends on: {[neighbor.value for neighbor in node.neighbors]}")
        
        queue.extend(node.neighbors)

# display_dependency_graph(clone)