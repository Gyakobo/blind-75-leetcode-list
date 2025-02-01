from clone_directed_graph import graph, Node, display_dependency_graph

root = graph.get_root_node()

def clone_directed_graph(root = root):
    oldToNew = {Node: Node} # Old : New

    def dfs(head):
        if head in oldToNew:
            return oldToNew[head]

        copy = Node(head.value)
        oldToNew[head] = copy
        for nei in head.neighbors: 
            copy.neighbors.append(dfs(nei))

        return copy

    return dfs(root)

cloned_graph = clone_directed_graph(root)
display_dependency_graph(cloned_graph)
