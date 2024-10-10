## Breadth-First Search (BFS) algorithm implementation in Python
# This implementation assumes that the graph is represented as an adjacency list

"""
Traversing graph has only issue that graph may have cycle. You may revisit a node.
To avoid processing a node more than once, we divide the vertices into two categories:
*  visited
*  Not visited
"""

# Import the necessary data structures
from collections import deque


def bfs(graph, start):
    # Create a queue for BFS and mark the start node as visited
    queue = deque([start])
    visited = set([start])

    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(vertex, end=" ")

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
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

# Call BFS
bfs(graph, 'A')
