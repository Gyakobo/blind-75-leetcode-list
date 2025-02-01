class Node:
    def __init__(self, value):
        self.value = value
        self.next = []

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
            
            self.nodes[start].next.append(self.nodes[end])

    def get_root_node(self):
        return self.nodes.get(0, None)

    def display_graph(self):
        for node in self.nodes.values():
            print(f"Node {node.value}: {[neighbor.value for neighbor in node.next]}")

# Template edges
template = [ [0, 4], [4, 0], [4, 3], [0, 3], [3, 2], [4, 1], [1, 2], [2, 0], [0, 2] ]

print("Create the Original Graph")
graph = DirectedGraph(template)
graph.display_graph()

def clone_directed_graph(root: Node) -> Node:
    pass