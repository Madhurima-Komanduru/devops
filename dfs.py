def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes
    
    if node not in visited:
        print(node, end=" ")  # Print the node
        visited.add(node)  # Mark it as visited
        for neighbor in graph.get(node, []):  # Visit neighbors
            dfs(graph, neighbor, visited)

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Call DFS
dfs(graph, 'A')
