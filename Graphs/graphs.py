from search_graphs import dfs, bfs
from dijkstra import dijkstra

graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 7)],
    'D': [('A', 9)]
}

print("DFS: ")
dfs(graph,'A')
print("\nBFS: ")
bfs(graph,'A')

print("\nDijkstra: ")
print(dijkstra(graph, 'A'))