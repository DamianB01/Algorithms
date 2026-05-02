from collections import deque

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, node):
    visited = set()
    visited.add(node)
    queue = deque([node])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
