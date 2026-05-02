import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        curr_dist, curr_node = heapq.heappop(priority_queue)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances