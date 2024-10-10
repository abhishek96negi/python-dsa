"""
* DFS is Depth first search. The main difference between BFS and DFS is that the DFS uses stack in place of Queue.
"""

def dfs_iterative(graph, start):
    # Create a stack for DFS and mark the start node as visited
    stack = [start]
    visited = set([start])

    while stack:
        # Pop a vertex from stack
        vertex = stack.pop()
        print(vertex, end=" ")

        # Get all adjacent vertices of the popped vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call DFS
dfs_iterative(graph, 'A')
